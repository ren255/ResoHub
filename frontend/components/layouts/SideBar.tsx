import { ChartColumnBig, Home, Info } from "lucide-react";

export const SideBar = () => (
  <ul className="menu bg-base-200 rounded-box h-screen fixed left-0 top-0">
    <li>
      <a className="tooltip tooltip-right" data-tip="Home">
        <Home />
      </a>
    </li>
    <li>
      <a className="tooltip tooltip-right" data-tip="Details">
        <Info />
      </a>
    </li>
    <li>
      <a className="tooltip tooltip-right" data-tip="Stats">
        <ChartColumnBig />
      </a>
    </li>
  </ul>
);
