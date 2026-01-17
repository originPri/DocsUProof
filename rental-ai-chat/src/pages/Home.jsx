import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { Shield } from "lucide-react";

const Home = () => {
  const navigate = useNavigate();
  const { user } = useAuth();

  const goToChat = () => {
    if (user) navigate("/chat");
    else navigate("/auth");
  };

  return (
    <div className="min-h-screen bg-white flex flex-col">
      {/* ---------------- Top Bar ---------------- */}
      <header className="flex items-center justify-between px-6 py-4 border-b">
        <div className="flex items-center gap-2 font-semibold">
          <Shield className="w-5 h-5" />
          Rental Checker
        </div>

        <div className="flex items-center gap-4">
          <button
            onClick={() => navigate("/auth")}
            className="text-sm font-medium text-gray-700"
          >
            Log in
          </button>
          <button
            onClick={() => navigate("/auth")}
            className="bg-black text-white text-sm px-4 py-2 rounded-full"
          >
            Sign up for free
          </button>
        </div>
      </header>

      {/* ---------------- Center Content ---------------- */}
      <main className="flex-1 flex flex-col items-center justify-center px-4">
        <h1 className="text-3xl md:text-4xl font-semibold mb-10">
          Ready when you are.
        </h1>

        {/* Prompt Box */}
        <div
          onClick={goToChat}
          className="w-full max-w-2xl border rounded-2xl px-4 py-3 flex items-center justify-between cursor-pointer hover:shadow-md transition"
        >
          <span className="text-gray-500">Ask anything about your rental agreement</span>

          <div className="flex items-center gap-2 text-sm text-gray-400">
            <span className="border px-2 py-1 rounded-md">Enter</span>
          </div>
        </div>

        {/* Helper text */}
        <p className="text-xs text-gray-400 mt-6 text-center max-w-md">
          Upload rental contracts, ask questions, and get AI-powered analysis
          based on Australian tenancy laws.
        </p>
      </main>

      {/* ---------------- Footer ---------------- */}
      <footer className="text-xs text-gray-400 text-center pb-4">
        By using Rental Checker, you agree to our Terms and Privacy Policy.
      </footer>
    </div>
  );
};

export default Home;
