import { Boxes, Home, Users } from "lucide-react";

export const SideBar = () => (
  <ul className="menu gap-4 w-16 bg-base-200 border-r h-screen fixed left-0 top-0 p-2">
    <li>
      <a
        href="/"
        className="tooltip tooltip-right flex items-center justify-center"
        data-tip="Home"
      >
        <Home size={24} />
      </a>
    </li>
    <li>
      <a
        href="/users"
        className="tooltip tooltip-right flex items-center justify-center"
        data-tip="User"
      >
        <Users size={24} />
      </a>
    </li>
    <li>
      <a
        href="/obj-search"
        className="tooltip tooltip-right flex items-center justify-center"
        data-tip="Objects search"
      >
        <Boxes size={24} />
      </a>
    </li>
  </ul>
);
