import { useState, useEffect } from "react";
import axios from "@/lib/axios/client";
import Artwork from "../types";

interface UseArtworksResult {
  artworks: Artwork[];
  loading: boolean;
  error: string | null;
}

const useArtworks = (): UseArtworksResult => {
  const [artworks, setArtworks] = useState<Artwork[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    // Function to fetch artworks
    const fetchArtworks = async () => {
      try {
        const response = await axios.get<Artwork[]>(`artworks/`);
        setArtworks(response.data);
        setLoading(false);
      } catch (err) {
        setError("Failed to load artworks");
        setLoading(false);
      }
    };

    fetchArtworks();
  }, []);

  return { artworks, loading, error };
};

export default useArtworks;