import { Button, Center, Title } from "@mantine/core"
import { NextPage } from "next"
import Link from "next/link"

const Home: NextPage = () => {
  return (
    <>
      <Title>
        This is the Home page
      </Title>

      <Center p={10}>
        <Link href='/users'>
          <Button>
            Move to Users page
          </Button>
        </Link>
      </Center>

      <Center p={10}>
        <Link href='/parts'>
          <Button>
            Move to Parts page
          </Button>
        </Link>
      </Center>
    </>
  )
}
export default Home