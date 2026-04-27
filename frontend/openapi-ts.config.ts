import { defineConfig } from "@hey-api/openapi-ts";

export default defineConfig({
	input: "http://resohub-backend:8000/api/schema/",
	output: "src/types/api/",
	plugins: [
		"@hey-api/client-axios",
		'@hey-api/sdk',
		"@hey-api/typescript",
	],
});
