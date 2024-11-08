import { Button } from "@/components/ui/button"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import Link from "next/link"

const InfoPanel = () => {
    return (
        <div className="w-80 p-4">
        <Input className="mb-4 bg-black" placeholder="Search" />
        <Card className="mb-4 bg-black">
          <CardHeader>
            <CardTitle>Subscribe to Premium</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="mb-2 text-sm">Subscribe to unlock new features and if eligible, receive a share of revenue.</p>
            <Button 
            className="mt-4 w-1/2 bg-[#F2C14E] font-semibold text-black px-5 py-3 hover:bg-yellow-500 transition-colors shadow-[0_0_15px_rgba(242,193,78,0.6)] hover:shadow-[0_0_20px_rgba(242,193,78,0.8)] rounded-3xl">Subscribe</Button>
          </CardContent>
        </Card>
        <Card className="bg-black">
          <CardHeader>
            <CardTitle>What's happening</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              <div>
                <p className="text-sm text-gray-500">Trending in United Kingdom</p>
                <p className="font-bold">--</p>
                <p className="text-sm text-gray-500">-- posts</p>
              </div>
              <div>
                <p className="text-sm text-gray-500">Politics · Trending</p>
                <p className="font-bold">--</p>
                <p className="text-sm text-gray-500">-- posts</p>
              </div>
              <div>
                <p className="text-sm text-gray-500">Trending in United Kingdom</p>
                <p className="font-bold">--</p>
                <p className="text-sm text-gray-500">-- posts</p>
              </div>
              <div>
                <Link href={'/'} className="mt-4 w-full justify-start text-[#F2C14E] text-sm">
                  Show more
                </Link>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>
    )

}

export default InfoPanel