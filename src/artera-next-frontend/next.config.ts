// next.config.ts
import { NextConfig } from "next";
import dotenv from "dotenv";
import path from "path";

dotenv.config({ path: path.resolve(__dirname, "../../../.env") });

const nextConfig: NextConfig = {
  env: {
    REACT_APP_API_BASE_URL: process.env.REACT_APP_API_BASE_URL,
  },
  images: {
    domains: ['d2w8kbdekdi1gv.cloudfront.net', 'naturalist.gallery'],
  },
  webpack(config) {
    config.module.rules.push({
      test: /\.svg$/,
      use: ['@svgr/webpack'],
    });
    return config;
  },
};

export default nextConfig;