import "../src/App.css";

function StrategiesBox({ onOpen }) {
    return(
        <button className="dashboard-box" onClick={onOpen}>
            <div className="box-heading">
                <span className="box-icon">▥</span>
                <h2>Strategy</h2>
                <span className="arrow"></span>
            </div>

            <div className="strategy-summary">
                <p>Current Strategy</p>
                <strong>Up and Down</strong>

                <div className="strategy-rules">
                    <div>
                        <p>Risk per Trade</p>
                        <span>1 - 2%</span>
                    </div>

                    <div>
                        <p>Target</p>
                        <span>5%</span>
                    </div>
                </div>
            </div>
        </button>
    );
}

export default StrategiesBox;