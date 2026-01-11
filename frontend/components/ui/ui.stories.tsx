import { Card } from "./Card";
import UserModal from "./UserModal";

export const Card_ = () => <Card />;

interface User {
  uuid: string;
  username: string;
  email: string;
  is_staff: boolean;
  is_superuser: boolean;
  date_joined: string;
}

export const UserModal_ = () => (
  <UserModal
    user={{
      uuid: "550e8400-e29b-41d4-a716-446655440000",
      username: "tanaka_taro",
      email: "tanaka.taro@example.com",
      is_staff: true,
      is_superuser: false,
      date_joined: "2024-01-15T09:30:00Z",
    }}
    isOpen={true}
    onClose={() => console.log("Modal closed")}
  />
);
