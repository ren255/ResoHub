export interface User {
  uuid: string;
  username: string;
  email: string;
  is_staff: boolean;
  is_superuser: boolean;
  date_joined: string;
}

export interface UserListResponse {
  data: User[];
  total: number;
}

export interface UseUsersReturn {
  users: User[];
  loading: boolean;
  error: string | null;
  refetch: () => Promise<void>;
}
