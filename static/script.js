// Check logic inside fetchStudents or on load
if (CURRENT_USER_ROLE === 'admin') {
    document.getElementById('adminPanel').style.display = 'block';
    loadAdminApprovals();
}

async function loadAdminApprovals() {
    const res = await fetch('/api/admin/approvals');
    const data = await res.json();
    
    // 1. Render Pending Users
    const userList = document.getElementById('pendingUsersList');
    userList.innerHTML = data.users.map(u => `
        <li style="background:white; margin:5px; padding:10px; display:flex; justify-content:space-between;">
            <span>${u.username}</span>
            <div>
                <button onclick="decideUser(${u.id}, 'approve')" style="color:green">✔</button>
                <button onclick="decideUser(${u.id}, 'reject')" style="color:red">✖</button>
            </div>
        </li>
    `).join('') || '<p>No pending users</p>';

    // 2. Render Pending Changes
    const changeList = document.getElementById('pendingChangesList');
    changeList.innerHTML = data.changes.map(c => `
        <li style="background:white; margin:5px; padding:10px;">
            <div><strong>${c.request_type}</strong> by ${c.username}</div>
            <div style="font-size:0.8rem; color:#666">${JSON.stringify(JSON.parse(c.new_data))}</div>
            <div style="margin-top:5px;">
                <button onclick="decideChange(${c.id}, 'approve')" class="btn-primary" style="padding:2px 10px; font-size:0.8rem">Approve</button>
                <button onclick="decideChange(${c.id}, 'reject')" style="color:red; background:none; border:none; cursor:pointer;">Reject</button>
            </div>
        </li>
    `).join('') || '<p>No pending changes</p>';
}

async function decideUser(id, action) {
    await fetch(`/api/admin/users/${id}/${action}`, { method: 'POST' });
    loadAdminApprovals();
}

async function decideChange(id, action) {
    if(action === 'approve') {
        await fetch(`/api/admin/changes/${id}/approve`, { method: 'POST' });
    } else {
        // You would implement a reject route similar to the approve one
        console.log("Rejected"); 
    }
    loadAdminApprovals();
    fetchStudents(); // Refresh main table
}