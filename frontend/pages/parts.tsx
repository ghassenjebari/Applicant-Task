import { NextPage } from "next"

import { Button, Stack, Title } from "@mantine/core"
import Link from "next/link"
import PartList from "@/components/partList"

const Parts: NextPage = () => {

    return (
        <>
            <Title>
                This is the Parts page
            </Title>
            <Stack h="100%" w="100%" align="center">
                <PartList />
                <Link href='/' >
                    <Button>
                        Back
                    </Button>
                </Link>
            </Stack>
        </>
    )
}
export default Parts