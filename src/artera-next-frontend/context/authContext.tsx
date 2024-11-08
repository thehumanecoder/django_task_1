import React, { createContext, useContext, useEffect, useState, ReactNode } from "react"
import Cookies from "js-cookie"
// import { useAuth } from "./useAuth"

interface AuthContextType {
  isAuthenticated: boolean
  setAuth: (token: string) => void
}

const AuthContext = createContext<AuthContextType | undefined>(undefined)

interface AuthProviderProps {
  children: ReactNode
}

export const AuthProvider: React.FC<AuthProviderProps> = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState<boolean>(!!Cookies.get("token"))
//   const { login, register } = useAuth()

  const setAuth = (token: string) => {
    // Set the token as a cookie and update isAuthenticated state
    Cookies.set("token", token)
    setIsAuthenticated(true)
  }

  // Check if token is present in cookies on mount to set isAuthenticated
  useEffect(() => {
    const token = Cookies.get("token")
    setIsAuthenticated(!!token)
  }, [])

  return (
    <AuthContext.Provider value={{ isAuthenticated, setAuth }}>
      {children}
    </AuthContext.Provider>
  )
}

// Hook to use the AuthContext in components
export const useAuthContext = () => {
  const context = useContext(AuthContext)
  if (!context) {
    throw new Error("useAuthContext must be used within an AuthProvider")
  }
  return context
}