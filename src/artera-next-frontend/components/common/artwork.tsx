import React from "react";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { Button } from "@/components/ui/button";
import { Bookmark, MoreHorizontal, MessageCircle, Heart } from "lucide-react";
import Image from "next/image";
import { Artwork as ArtworkType } from '@/types';
import Link from "next/link";

interface SocialPostProps {
  artwork?: ArtworkType;  // Making artwork optional to prevent destructuring errors
}

const Artwork: React.FC<SocialPostProps> = ({ artwork }) => {
  if (!artwork) return null; 

  const { 
    profile, 
    artwork_name, 
    artwork_description, 
    artwork_images, 
    artwork_likes_counter, 
    artwork_comments_counter, 
    artwork_views_counter 
  } = artwork;

  return (
    <div className="p-4">
      <div className="border-b border-[#2E3234] pt-4">
        <div className="mb-4">
          <div className="flex items-center justify-between">
            <Link href={`/user/${profile?.profile_handle}`}>
              <div className="flex items-center space-x-2">
                <Avatar>
                  <AvatarImage src={profile?.profile_picture.main_300} />
                  <AvatarFallback>{profile?.profile_handle.charAt(0).toUpperCase()}</AvatarFallback>
                </Avatar>
                <div>
                  <span className="font-bold">{profile?.profile_handle}</span>
                  <span className="text-[#71767A]"> @{profile?.user}</span>
                </div>
              </div>              
            </Link>

            <Button variant="ghost" size="sm">
              <MoreHorizontal className="h-4 w-4" />
            </Button>
          </div>
          <p className="mt-2 font-semibold">{artwork_name}</p>
          <p className="mt-2">{artwork_description}</p>
          <Image
            src={artwork_images.main_600}
            height={artwork.artwork_main_image_height}
            width={artwork.artwork_main_image_width}
            alt={artwork_name}
            className="mt-2 rounded-xl"
          />
          <div className="mt-2 flex justify-between text-[#71767A]">
            <Button variant="ghost" size="sm">
              <Heart /> {artwork_likes_counter}
            </Button>
            <Button variant="ghost" size="sm">
              <MessageCircle /> {artwork_comments_counter}
            </Button>
            <Button variant="ghost" size="sm">
              <Bookmark /> {artwork_views_counter}
            </Button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Artwork;