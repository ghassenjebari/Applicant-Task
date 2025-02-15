import { Button, Center, Title, Text, Stack } from "@mantine/core";
import { NextPage } from "next";
import Link from "next/link";
import Head from "next/head";

const Home: NextPage = () => {
  return (
    <>
      <Head>
        <title>RFA TECHNICAL TEST</title>
      </Head>

      <div className="main-content">
        <Stack align="center" spacing="md">

          <Title order={1} className="hero-title">
            RFA🚀
          </Title>

          <Text className="hero-subtitle">
          Welcome to the internal dashboard
          </Text>
          <Link href="/parts">
           
          </Link>
        </Stack>
      </div>
    </>
  );
};

export default Home;
