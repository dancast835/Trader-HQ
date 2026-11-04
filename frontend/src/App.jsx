import { useState} from "react";
import AccountBox from "../components/accountBox.jsx";
import StrategiesBox from "../components/strategiesBox.jsx";
import "./App.css";

function App() {
    const [openBox, setOpenBox] = useState(null);

    function closeBox() {
        setOpenBox(null);
    }

    return (
        <main className="dashboard">
            <header className="dashboard-header">
                <h1>Trader HQ</h1>
            </header>

            <section className="dashboard-grid">
                <AccountBox onOpen={() => setOpenBox("account")} />
                <StrategiesBox onOpen={() => setOpenBox("strategy")} />
            </section>

            {/* what is the function of && ???? */}
            {openBox && (
                <div className="modal-overlay" onClick={closeBox}>
                    <section
                        className="expanded-box"

                        onClick={(event) => event.stopPropagation()}
                    >
                        <div className="expanded-box-header">
                            <h2>{openBox}</h2>

                            <button className="close-button" onClick={closeBox} aria-label="Close">
                                x
                            </button>
                        </div>

                        <div className="expanded-box-content"></div>
                    </section>
                </div>
            )}
        </main>
    );
}

export default App;

