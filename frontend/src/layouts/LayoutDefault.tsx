import "./style.css";
import "./tailwind.css";

import { SideBar } from "@/components/layouts/SideBar";
import { Outlet } from "react-router-dom";

export default function LayoutDefault() {
  return (
    <div className="flex">
      <SideBar />
      <Content>
        <Outlet />
      </Content>
    </div>
  );
}

function Content({ children }: { children: React.ReactNode }) {
  return (
    <div id="page-container" className="ml-16 flex-1">
      <div id="page-content" className="p-5 pb-12 min-h-screen">
        {children}
      </div>
    </div>
  );
}

