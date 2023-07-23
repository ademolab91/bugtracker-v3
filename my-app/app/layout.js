import { AuthContextProvider } from "@/auth/context";
import "./globals.css";
import { Source_Sans_3 } from "next/font/google";

const source = Source_Sans_3({ subsets: ["latin"] });

export const metadata = {
  title: "Create Next App",
  description: "Generated by create next app",
};

export default function RootLayout({ children }) {
  return (
    <html data-theme="forest" lang="en">
      <AuthContextProvider>
        <body className={source.className}>{children}</body>
      </AuthContextProvider>
    </html>
  );
}
