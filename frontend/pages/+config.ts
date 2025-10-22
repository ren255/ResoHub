import type { Config } from "vike/types";
import vikeReact from "vike-react/config";
import Layout from "../layouts/LayoutDefault.js";
import * as Sentry from "@sentry/browser";

// Sentryの初期化
Sentry.init({
  dsn: "https://76a0d90506c14728b646ea7542901ebd@glitchtip:8000/2",
});

// Default config (can be overridden by pages)
// https://vike.dev/config

export default {
  // https://vike.dev/Layout
  Layout,

  // https://vike.dev/head-tags
  title: "My Vike App",
  description: "Demo showcasing Vike",

  extends: vikeReact,
} satisfies Config;
