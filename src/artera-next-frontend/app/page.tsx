import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { ScrollArea } from "@/components/ui/scroll-area"
import { Bell, Bookmark, Hash, Home, Mail, MoreHorizontal, Search, User, Zap } from "lucide-react"
import Image from "next/image"
import Artwork from '@/components/common/artwork'
import Feed from '@/components/layout/feed'
import logo from '@/public/logo.png'

export default function Page() {
  return (
  <div className="flex-1 border-r border-[#2E3234]">
    <div className="border-b border-[#2E3234] p-4">
      <h1 className="text-xl font-bold">Home</h1>
    </div>
    <Feed />
  </div>
  )
}