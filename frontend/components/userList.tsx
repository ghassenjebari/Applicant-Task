import { getUsers } from "@/data/dataHandler"
import { List } from "@mantine/core"
import { useEffect, useState } from "react"

const UserList = () => {
    const [users, setUsers] = useState<User[]>([])

    useEffect(() => {
        const initData = async () => {
            const users = await getUsers()
            setUsers(users)
        }
        initData()
    }, [])

    return (
        <List>
            {users.map((user, idx) => {
                return (
                    <List.Item key={idx}>
                        ID: {user.id}
                        Name: {user.name}
                    </List.Item>
                )
            })}
        </List>
    )
}
export default UserList