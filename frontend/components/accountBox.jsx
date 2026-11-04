import "../src/App.css";

function AccountBox({ onOpen }) {
    return (
        <button className="dashboard-box" onClick={onOpen}>
            <div className="box-heading">
                <span className="box-icon">▣</span>
                <h2>Account</h2>
                <span className="arrow"></span>
            </div>

            <div className="account-summary">
                <div>
                    <p>Portfolio Balance</p>
                    <strong>$1,000</strong>
                </div>

                <div>
                    <p>Daily P/L</p>
                    <strong className="profit">+$348.21</strong>
                </div>

                <div>
                    <p>Buying Power</p>
                    <strong>$2,000</strong>
                </div>
            </div>
        </button>
    );
}

export default AccountBox;