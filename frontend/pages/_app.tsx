import { AppProps } from 'next/app';
import Head from 'next/head';
import { MantineProvider } from '@mantine/core';
import Navbar from "@/components/Navbar"; 
import "@/styles/globals.css"; 

export default function App({ Component, pageProps }: AppProps) {
  return (
    <>
      <Head>
        <title>Test Project</title>
        <meta name="viewport" content="minimum-scale=1, initial-scale=1, width=device-width" />
      </Head>

      <MantineProvider withGlobalStyles withNormalizeCSS>

        <Navbar /> 
        
       
        <div className="main-content">
          <Component {...pageProps} /> 
        </div>

      </MantineProvider>
    </>
  );
}
