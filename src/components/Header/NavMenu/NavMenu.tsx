import { useState, useEffect } from 'react';

const NavMenu = () => {
  const [isOpen] = useState(false);

  useEffect(() => {
    console.log('isOpen:', isOpen);
  }, [isOpen]);

  return (
    <div>
      {/* Your component JSX here */}
    </div>
  );
};

export default NavMenu;
