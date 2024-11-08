export default interface Artwork {
  artwork_id: string
  profile: Profile
  artwork_type: string
  artwork_privacy: string
  artwork_name: string
  artwork_date: string
  artwork_images: ArtworkImages
  artwork_location: string
  artwork_description: string
  artwork_likes_counter: number
  artwork_comments_counter: number
  artwork_views_counter: number
  artwork_collections_counter: number
  artwork_shares_counter: number
  artwork_main_image_height: number
  artwork_main_image_width: number
}

export interface Profile {
  id: number
  profile_picture: ProfilePicture
  profile_handle: string
  user: number
}

export interface ProfilePicture {
  source: string
  main_300: string
  main_600: string
  main_1920: string
}

export interface ArtworkImages {
  source: string
  main_300: string
  main_600: string
  main_1920: string
}
