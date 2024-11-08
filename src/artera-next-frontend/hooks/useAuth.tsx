"use client"
import { useState } from "react"
import axios from "@/lib/axios/client"
import Cookies from "js-cookie"
import jwt_decode from "jwt-decode"

interface UseAuthResponse {
  register: (email: string, password: string, profile_handle: string) => Promise<void>
  login: (email: string, password: string) => Promise<void>
  isAuthenticated: boolean
}

interface JWTToken {
  exp: number
}

export function useAuth(): UseAuthResponse {
  const [isAuthenticated, setIsAuthenticated] = useState<boolean>(!!Cookies.get("token"))

  const setAuthToken = (token: string) => {
    const decodedToken = jwt_decode<JWTToken>(token)
    const expirationDate = new Date(decodedToken.exp * 1000)
    Cookies.set("token", token, { expires: expirationDate })
    setIsAuthenticated(true)
  }

  const setRefreshToken = (token: string) => {
    const decodedToken = jwt_decode<JWTToken>(token)
    const expirationDate = new Date(decodedToken.exp * 1000)
    Cookies.set("refreshToken", token, { expires: expirationDate })
    setIsAuthenticated(true)
  }

  const register = async (email: string, password: string, profile_handle: string) => {
    try {
      // Use axios to make the registration API call
      const response = await axios.post("/accounts/register/", { profile_handle, email, password })

      if (response.status == 201 && response.data) {
        setAuthToken(response.data.access)
        setRefreshToken(response.data.refresh)
        return response
      }
      
    } catch (error) {
      console.error("Registration error:", error)
    }
  }

  const login = async (email: string, password: string) => {
    try {
      // Use axios to make the login API call
      const response = await axios.post("/accounts/login/", { email, password })

      if (response.status == 200 && response.data.token) {
        setAuthToken(response.data.token)
        setRefreshToken(response.data.refresh)
        return response
      }
    } catch (error) {
      console.error("Login error:", error)
    }
  }

  return {
    register,
    login,
    isAuthenticated,
  }
}