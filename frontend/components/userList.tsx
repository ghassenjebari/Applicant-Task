import { getUsers } from "@/data/dataHandler";
import { useEffect, useState } from "react";
import { Modal, Button, Loader, Stack, Title, Text } from "@mantine/core";
import addPartForm from "@/components/addPartForm";
import ItemCard from "@/components/ItemCard"; // 


const UserList = () => {
    const [users, setUsers] = useState<User[]>([]);
    const [loading, setLoading] = useState<boolean>(true);
    const [opened, setOpened] = useState(false);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const users = await getUsers();
                setUsers(users);
            } catch (error) {
            } finally {
                setLoading(false);
            }
        };
        fetchData();
    }, []);

    return (
        <Stack spacing="lg" align="center" w="100%">
         <Title order={2} style={{ color: "white" }}> Users </Title>

            {loading ? (
                <Loader color="blue" size="lg" />
            ) : users.length === 0 ? (
                <Text color="dimmed" size="md">No user found.</Text>
            ) : (
                <div className="user-grid">
                    {users.map((user) => (
                        <ItemCard key={user.id} id={user.id} name={user.name}  type="user" />
                    ))}
                </div>
            )}
        </Stack>
    );
};

export default UserList;
