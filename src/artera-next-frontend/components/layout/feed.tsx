"use client";

import React from "react";
import Artwork from "../common/artwork";
import useArtworks from "@/hooks/useArtworks";
import { ScrollArea } from "@/components/ui/scroll-area";

interface FeedProps {
  scrollarea?: boolean;
}

const Feed: React.FC<FeedProps> = ({ scrollarea = true }) => {
  const { artworks, loading, error } = useArtworks();

  if (loading) return <p>Loading...</p>;
  if (error) return <p>{error}</p>;

  return (
    <>
      {scrollarea ? (
        <ScrollArea className="h-[calc(100vh-60px)]">
          {artworks && artworks.map((artwork) => (
            <Artwork key={artwork.artwork_id} artwork={artwork} />
          ))}
        </ScrollArea>
      ) : (
        <div>
          {artworks && artworks.map((artwork) => (
            <Artwork key={artwork.artwork_id} artwork={artwork} />
          ))}
        </div>
      )}
    </>
  );
};

export default Feed;