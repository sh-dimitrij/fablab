import "./Hamburger.sass"

// src/components/Header/NavMenu/Hamburger/Hamburger.tsx

const Hamburger = ({ isOpen, setIsOpen }: { isOpen: boolean; setIsOpen: (value: boolean) => void }) => {
	return (
	  <div className={"hamburger-wrapper " + (isOpen ? "open" : "")} onClick={() => setIsOpen(!isOpen)}>
		{/* ... */}
	  </div>
	);
  };
  
  export default Hamburger;
  