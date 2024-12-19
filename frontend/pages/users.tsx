import { NextPage } from "next"

import UserList from "@/components/userList"
import { Button, Stack, Title } from "@mantine/core"
import Link from "next/link"

const Users: NextPage = () => {


    return (
        <>
            <Title>
                This is the Parts page
            </Title>
            <Stack h="100%" w="100%" align="center">
                <UserList />
                <Link href='/' >
                    <Button>
                        Back
                    </Button>
                </Link>
            </Stack>
        </>
    )
}
export default Users