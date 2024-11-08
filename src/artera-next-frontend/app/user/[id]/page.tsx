"use client"

import React from 'react'
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { ScrollArea } from "@/components/ui/scroll-area"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { Bell, Bookmark, ChevronLeft, Hash, Home, Mail, MoreHorizontal, Search, User, Zap } from "lucide-react"
import Image from "next/image"
import Feed from '@/components/layout/feed'

export default function Page() {


  return (
    <div className="flex-1 border-r border-gray-800">
    <div className="border-b border-gray-800 p-4 flex items-center">
        <Button variant="ghost" size="sm" className="mr-4">
        <ChevronLeft className="h-5 w-5" />
        </Button>
        <div>
        <h1 className="text-xl font-bold">Leonardo da Vinci</h1>
        </div>
    </div>
    <ScrollArea className="h-[calc(100vh-60px)]">
        <div className="relative">
        <Image
            src="https://naturalist.gallery/cdn/shop/articles/adrianna-geo-1rBg5YSi00c-unsplash_2.jpg?v=1691115092&width=1100"
            height={200}
            width={600}
            alt="Cover Photo"
            className="w-full h-48 object-cover"
        />
        <Avatar className="absolute bottom-0 left-4 transform translate-y-1/2 border-4 border-black w-32 h-32">
            <AvatarImage src="https://hips.hearstapps.com/hmg-prod/images/portrait-of-leonardo-da-vinci-1452-1519-getty.jpg" alt="Leonardo" />
            <AvatarFallback>DA</AvatarFallback>
        </Avatar>
        </div>
        <div className="p-4 pt-20">
        <div className="flex justify-between items-start mb-4">
            <div>
            <h2 className="text-2xl font-bold">Leonardo da Vinci</h2>
            <p className="text-gray-500">@Leonardo</p>
            </div>
            <Button className="bg-[#F2C14E] font-semibold text-black px-5 py-3 hover:bg-yellow-500 transition-colors shadow-[0_0_15px_rgba(242,193,78,0.6)] hover:shadow-[0_0_20px_rgba(242,193,78,0.8)] rounded-3xl">Follow</Button>
        </div>
        <p className="mb-2">Hello world</p>
        <p className="text-[#F2C14E] mb-2">artera.ae</p>
        <p className="text-gray-500 mb-4">Joined June 2009</p>
        <div className="flex space-x-4 text-gray-500 mb-4">
            <span><strong className="text-white">797</strong> Following</span>
            <span><strong className="text-white">202.6M</strong> Followers</span>
            <span><strong className="text-white">175</strong> Subscriptions</span>
        </div>        
        <Feed scrollarea={false} />
        </div>
    </ScrollArea>

    </div>
  )
}