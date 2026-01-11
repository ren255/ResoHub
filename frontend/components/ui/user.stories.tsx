import { useState } from "react";
import UserTable from "./UserTable";
import UserModal from "./UserModal";
import { User } from "../../types/User";

const mockUsers: User[] = [
  {
    uuid: "123e4567-e89b-12d3-a456-426614174000",
    username: "admin_user",
    email: "admin@example.com",
    is_staff: true,
    is_superuser: true,
    date_joined: "2024-01-15T10:30:00Z",
  },
  {
    uuid: "123e4567-e89b-12d3-a456-426614174001",
    username: "staff_user",
    email: "staff@example.com",
    is_staff: true,
    is_superuser: false,
    date_joined: "2024-03-20T14:15:00Z",
  },
  {
    uuid: "123e4567-e89b-12d3-a456-426614174002",
    username: "normal_user",
    email: "user@example.com",
    is_staff: false,
    is_superuser: false,
    date_joined: "2024-06-10T09:00:00Z",
  },
];

export function UserTableStory() {
  const [selectedUser, setSelectedUser] = useState<User | null>(null);

  return (
    <div className="p-8">
      <h2 className="text-2xl font-bold mb-4">UserTable Story</h2>
      <UserTable
        users={mockUsers}
        isLoading={false}
        onUserClick={(user) => alert(`Clicked: ${user.username}`)}
      />
    </div>
  );
}

export function UserModalStory() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className="p-8">
      <h2 className="text-2xl font-bold mb-4">UserModal Story</h2>
      <button className="btn btn-primary" onClick={() => setIsOpen(true)}>
        モーダルを開く
      </button>
      <UserModal
        user={mockUsers[0]}
        isOpen={isOpen}
        onClose={() => setIsOpen(false)}
      />
    </div>
  );
}

export function UserTableWithModalStory() {
  const [selectedUser, setSelectedUser] = useState<User | null>(null);
  const [isModalOpen, setIsModalOpen] = useState(false);

  const handleUserClick = (user: User) => {
    setSelectedUser(user);
    setIsModalOpen(true);
  };

  return (
    <div className="p-8">
      <h2 className="text-2xl font-bold mb-4">UserTable + UserModal Story</h2>
      <UserTable
        users={mockUsers}
        isLoading={false}
        onUserClick={handleUserClick}
      />
      <UserModal
        user={selectedUser}
        isOpen={isModalOpen}
        onClose={() => setIsModalOpen(false)}
      />
    </div>
  );
}
