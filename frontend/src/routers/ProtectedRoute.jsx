import {Navigate} from "react-router-dom";

export default function ProtectedRoute({children}){
    const {user} = JSON.parse(localStorage.getItem("auth"));
    return auth.account ? <>{children}</>:<Navigate to="/login" />;
}