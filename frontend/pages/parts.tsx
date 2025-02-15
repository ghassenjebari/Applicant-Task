import { NextPage } from "next"

import { Button, Stack, Title } from "@mantine/core"
import Link from "next/link"
import PartList from "@/components/partList"
import AddPartForm from "@/components/addPartForm"

const Parts: NextPage = () => {

    return (
        <>
            
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