import { ChartColumnBig, Home, Info } from "lucide-react";

export const SideBar = () => (
  <ul className="menu gap-4 w-16 bg-base-200 border-r h-screen fixed left-0 top-0 p-2">
    <li>
      <a
        href="#home"
        className="tooltip tooltip-right flex items-center justify-center w-8 h-8"
        data-tip="Home"
      >
        <Home size={24} />
      </a>
    </li>
    <li>
      <a
        href="#details"
        className="tooltip tooltip-right flex items-center justify-center w-8 h-8"
        data-tip="Details"
      >
        <Info size={24} />
      </a>
    </li>
    <li>
      <a
        href="#stats"
        className="tooltip tooltip-right flex items-center justify-center w-8 h-8"
        data-tip="Stats"
      >
        <ChartColumnBig size={24} />
      </a>
    </li>
  </ul>
);
