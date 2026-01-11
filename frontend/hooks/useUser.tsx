import { useState, useEffect, useCallback } from "react";
import axios from "axios";
import { User, UseUsersReturn } from "../types/User";

export const useUsers = (): UseUsersReturn => {
  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const fetchUsers = useCallback(async () => {
    try {
      setLoading(true);
      setError(null);
      const response = await axios.get("/api/user/");
      setUsers(response.data);
    } catch (err) {
      setError("ユーザー情報の取得に失敗しました");
      console.error("Error fetching users:", err);
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchUsers();
  }, [fetchUsers]);

  return {
    users,
    loading,
    error,
    refetch: fetchUsers,
  };
};
