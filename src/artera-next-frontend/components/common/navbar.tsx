import React from 'react'
import { Button } from "@/components/ui/button"
import { Bell, Bookmark, Hash, Home, Mail, MoreHorizontal, Search, User, Zap } from "lucide-react"
import Image from "next/image"
import Link from 'next/link'
import logo from '@/public/logo.png'


const Navigation = () => {
    return (
    <div className="w-64 p-4 border-r border-[#2E3234]">
        <div className="mb-8">
          <Image src={logo} alt="Artera Logo" width={50} height={50} unoptimized={true} />
        </div>
        <nav className="space-y-4">
          <Link href={'/'}>
            <Button variant="ghost" className="w-full justify-start text-xl">
              <Home className="mr-4 h-6 w-6" />
              Home
            </Button>
          </Link>
          <Button 
          disabled={true}
          variant="ghost" className="w-full justify-start text-xl">
            <Hash className="mr-4 h-6 w-6" />
            Explore
          </Button>
          <Button 
          disabled={true}
          variant="ghost" className="w-full justify-start text-xl">
            <Bell className="mr-4 h-6 w-6" />
            Notifications
          </Button>
          <Button 
          disabled={true}
          variant="ghost" className="w-full justify-start text-xl">
            <Mail className="mr-4 h-6 w-6" />
            Messages
          </Button>
          <Button 
          disabled={true}
          variant="ghost" className="w-full justify-start text-xl">
            <Bookmark className="mr-4 h-6 w-6" />
            Collections
          </Button>
          <Button 
          variant="ghost" className="w-full justify-start text-xl">
            <User className="mr-4 h-6 w-6" />
            Profile
          </Button>
          <Button variant="ghost" className="w-full justify-start text-xl">
            <MoreHorizontal className="mr-4 h-6 w-6" />
            More
          </Button>
        </nav>
        <Button className="mt-4 w-full bg-[#F2C14E] rounded-[10px] font-semibold text-black px-5 py-3 hover:bg-yellow-500 transition-colors shadow-[0_0_15px_rgba(242,193,78,0.6)] hover:shadow-[0_0_20px_rgba(242,193,78,0.8)] rounded-3xl">Upload</Button>
    </div>
    )
}

export default Navigation