import { useState } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

import mainMD from "../../readme/README.md?raw";
import backendMD from "../../readme/backend-README.md?raw";
import frontendMD from "../../readme/frontend-README.md?raw";

export default function App() {
  const [selected, setSelected] = useState("main");

  // 選択中のMarkdownコンテンツを設定
  let content;
  if (selected === "main") content = mainMD;
  else if (selected === "frontend") content = frontendMD;
  else if (selected === "backend") content = backendMD;

  return (
    <div className="w-full min-h-screen flex flex-col py-8">
      <div>
        <div className="gap-4 mb-8 flex">
          <button className="btn" onClick={() => setSelected("main")}>
            main
          </button>
          <button className="btn" onClick={() => setSelected("frontend")}>
            frontend
          </button>
          <button className="btn" onClick={() => setSelected("backend")}>
            backend
          </button>
        </div>
        <div className="prose prose-lg max-w-4xl w-full px-4">
          <ReactMarkdown remarkPlugins={[remarkGfm]}>{content}</ReactMarkdown>
        </div>
      </div>
    </div>
  );
}
