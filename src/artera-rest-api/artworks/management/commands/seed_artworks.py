import random
import uuid
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from artworks.models import Artworks
from users.models import Profiles
from django.utils import timezone

class Command(BaseCommand):
    help = 'Seeds the database with random artworks and profiles'

    # Define random data for seeding
    titles = [
        "Urban Odyssey", "Neon Dreams", "Cyber Groove", "Mystic Vibes", "Electric Night",
        "Astral Beats", "Digital Mirage", "Future Pulse", "Eclipse Flow", "Virtual Escape",
        "Retro Wave", "Galactic Drift", "Quantum Realm", "Hyperspace Harmony", "Echoes of Tomorrow"
    ]
    
    descriptions = [
        "A vibrant exploration of urban culture.", "The beat of the city in neon hues.",
        "Where reality meets the digital realm.", "Uncover the mysteries of virtual worlds.",
        "An electric mix of future and fantasy.", "Exploring the pulse of the modern age.",
        "A digital masterpiece in every sense.", "Future beats with a retro vibe.",
        "An eclipse of sound and vision.", "Escaping into a new dimension."
    ]

    handles = [
        "dj_tech", "neon_night", "future_fox", "urban_art", "cyber_mystic", "pixel_king", 
        "rhythm_rider", "virtual_queen", "cosmic_wave", "beat_master", "astro_dreamer",
        "sonic_soul", "retro_rock", "quantum_beat", "hyper_wave"
    ]
    
    random_images = [
        'https://d2w8kbdekdi1gv.cloudfront.net/eyJidWNrZXQiOiAiYXJ0ZXJhLWltYWdlcy1idWNrZXQiLCAia2V5IjogImFydHdvcmtzLzIyMzFiNWI0LTU0MDUtNDQ4Yi1hZDYzLTEzZTJjM2RmZjZhOS8yMjMxYjViNC01NDA1LTQ0OGItYWQ2My0xM2UyYzNkZmY2YTlfZnVsbC5qcGciLCAiZWRpdHMiOiB7InJlc2l6ZSI6IHsid2lkdGgiOiAxOTIwLCAiaGVpZ2h0IjogMTkyMCwgImZpdCI6ICJpbnNpZGUifX19',
        'https://d2w8kbdekdi1gv.cloudfront.net/eyJidWNrZXQiOiAiYXJ0ZXJhLWltYWdlcy1idWNrZXQiLCAia2V5IjogImFydHdvcmtzLzEwNWFlZjE4LTBlMTMtNGU5MC05ZmM1LTFjMmRmYTYwMmRjMC8xMDVhZWYxOC0wZTEzLTRlOTAtOWZjNS0xYzJkZmE2MDJkYzBfZnVsbC5qcGciLCAiZWRpdHMiOiB7InJlc2l6ZSI6IHsid2lkdGgiOiAxOTIwLCAiaGVpZ2h0IjogMTkyMCwgImZpdCI6ICJpbnNpZGUifX19',
        'https://d2w8kbdekdi1gv.cloudfront.net/eyJidWNrZXQiOiAiYXJ0ZXJhLWltYWdlcy1idWNrZXQiLCAia2V5IjogImFydHdvcmtzLzI5Mzc0MmIzLTUxMGUtNDE4ZS1iMmI3LTQ2YzU5ZjZlMTkwZi8yOTM3NDJiMy01MTBlLTQxOGUtYjJiNy00NmM1OWY2ZTE5MGZfZnVsbC5qcGciLCAiZWRpdHMiOiB7InJlc2l6ZSI6IHsid2lkdGgiOiAxOTIwLCAiaGVpZ2h0IjogMTkyMCwgImZpdCI6ICJpbnNpZGUifX19',
        'https://d2w8kbdekdi1gv.cloudfront.net/eyJidWNrZXQiOiAiYXJ0ZXJhLWltYWdlcy1idWNrZXQiLCAia2V5IjogImFydHdvcmtzL2I2MjgwOTVlLTYzMGItNDg4Yi05NjBiLTUxOTJiNmM2ZGFhOC9iNjI4MDk1ZS02MzBiLTQ4OGItOTYwYi01MTkyYjZjNmRhYThfZnVsbC5qcGciLCAiZWRpdHMiOiB7InJlc2l6ZSI6IHsid2lkdGgiOiAxOTIwLCAiaGVpZ2h0IjogMTkyMCwgImZpdCI6ICJpbnNpZGUifX19',
        'https://d2w8kbdekdi1gv.cloudfront.net/eyJidWNrZXQiOiAiYXJ0ZXJhLWltYWdlcy1idWNrZXQiLCAia2V5IjogImFydHdvcmtzL2NhMGU1ZjNiLTc1YmUtNGE0MC05MTI4LWQ0MTEyODYwZTVmNi9jYTBlNWYzYi03NWJlLTRhNDAtOTEyOC1kNDExMjg2MGU1ZjZfZnVsbC5qcGciLCAiZWRpdHMiOiB7InJlc2l6ZSI6IHsid2lkdGgiOiAxOTIwLCAiaGVpZ2h0IjogMTkyMCwgImZpdCI6ICJpbnNpZGUifX19',
        'https://d2w8kbdekdi1gv.cloudfront.net/eyJidWNrZXQiOiAiYXJ0ZXJhLWltYWdlcy1idWNrZXQiLCAia2V5IjogImFydHdvcmtzL2QwM2Q5MjU0LWNiZTItNGIyZi05Njc0LTk2MmEwY2U4YTRlYS9kMDNkOTI1NC1jYmUyLTRiMmYtOTY3NC05NjJhMGNlOGE0ZWFfZnVsbC5qcGciLCAiZWRpdHMiOiB7InJlc2l6ZSI6IHsid2lkdGgiOiAxOTIwLCAiaGVpZ2h0IjogMTkyMCwgImZpdCI6ICJpbnNpZGUifX19',
        'https://d2w8kbdekdi1gv.cloudfront.net/eyJidWNrZXQiOiAiYXJ0ZXJhLWltYWdlcy1idWNrZXQiLCAia2V5IjogImFydHdvcmtzLzE1M2EwMWFiLWNhMzEtNGMxOC1iYjdiLTBkNWI3NmQ5NDM1Zi8xNTNhMDFhYi1jYTMxLTRjMTgtYmI3Yi0wZDViNzZkOTQzNWZfZnVsbC5qcGciLCAiZWRpdHMiOiB7InJlc2l6ZSI6IHsid2lkdGgiOiAxOTIwLCAiaGVpZ2h0IjogMTkyMCwgImZpdCI6ICJpbnNpZGUifX19',
        'https://d2w8kbdekdi1gv.cloudfront.net/eyJidWNrZXQiOiAiYXJ0ZXJhLWltYWdlcy1idWNrZXQiLCAia2V5IjogImFydHdvcmtzLzE2MWNlODk0LTlkNDctNDc5My1hMmFmLTU2NjIzZTJkZGE3OS8xNjFjZTg5NC05ZDQ3LTQ3OTMtYTJhZi01NjYyM2UyZGRhNzlfZnVsbC5qcGciLCAiZWRpdHMiOiB7InJlc2l6ZSI6IHsid2lkdGgiOiAxOTIwLCAiaGVpZ2h0IjogMTkyMCwgImZpdCI6ICJpbnNpZGUifX19',
        'https://d2w8kbdekdi1gv.cloudfront.net/eyJidWNrZXQiOiAiYXJ0ZXJhLWltYWdlcy1idWNrZXQiLCAia2V5IjogImFydHdvcmtzLzVhODU1Y2ZlLTZjZjktNDgxOC05OGRkLWUxNjVmMDY1MmFhZC81YTg1NWNmZS02Y2Y5LTQ4MTgtOThkZC1lMTY1ZjA2NTJhYWRfZnVsbC5qcGciLCAiZWRpdHMiOiB7InJlc2l6ZSI6IHsid2lkdGgiOiAxOTIwLCAiaGVpZ2h0IjogMTkyMCwgImZpdCI6ICJpbnNpZGUifX19',
        'https://d2w8kbdekdi1gv.cloudfront.net/eyJidWNrZXQiOiAiYXJ0ZXJhLWltYWdlcy1idWNrZXQiLCAia2V5IjogImFydHdvcmtzL2U0NzRmOTE1LWFmODAtNDQ0OS05Zjg4LTg0NzIwZDA4N2E3Ni9lNDc0ZjkxNS1hZjgwLTQ0NDktOWY4OC04NDcyMGQwODdhNzZfZnVsbC5qcGciLCAiZWRpdHMiOiB7InJlc2l6ZSI6IHsid2lkdGgiOiAxOTIwLCAiaGVpZ2h0IjogMTkyMCwgImZpdCI6ICJpbnNpZGUifX19',
        'https://d2w8kbdekdi1gv.cloudfront.net/eyJidWNrZXQiOiAiYXJ0ZXJhLWltYWdlcy1idWNrZXQiLCAia2V5IjogImFydHdvcmtzLzFjM2VjNzM3LWRlMTAtNDU4Zi04NjUzLTRjZGVjMjRlODk4Mi8xYzNlYzczNy1kZTEwLTQ1OGYtODY1My00Y2RlYzI0ZTg5ODJfZnVsbC5qcGciLCAiZWRpdHMiOiB7InJlc2l6ZSI6IHsid2lkdGgiOiAxOTIwLCAiaGVpZ2h0IjogMTkyMCwgImZpdCI6ICJpbnNpZGUifX19',
        'https://d2w8kbdekdi1gv.cloudfront.net/eyJidWNrZXQiOiAiYXJ0ZXJhLWltYWdlcy1idWNrZXQiLCAia2V5IjogImFydHdvcmtzLzAwNWZlNDM2LTExOTktNDc5NC1iOTc4LTM3YmZlNDE0ODVhMi8wMDVmZTQzNi0xMTk5LTQ3OTQtYjk3OC0zN2JmZTQxNDg1YTJfZnVsbC5qcGciLCAiZWRpdHMiOiB7InJlc2l6ZSI6IHsid2lkdGgiOiAxOTIwLCAiaGVpZ2h0IjogMTkyMCwgImZpdCI6ICJpbnNpZGUifX19',
        'https://d2w8kbdekdi1gv.cloudfront.net/eyJidWNrZXQiOiAiYXJ0ZXJhLWltYWdlcy1idWNrZXQiLCAia2V5IjogImFydHdvcmtzLzNhZmYzMTAyLTUyNTItNDYwNy1hZDIwLWJiMGM2NGUyYmM1YS8zYWZmMzEwMi01MjUyLTQ2MDctYWQyMC1iYjBjNjRlMmJjNWFfZnVsbC5qcGciLCAiZWRpdHMiOiB7InJlc2l6ZSI6IHsid2lkdGgiOiAxOTIwLCAiaGVpZ2h0IjogMTkyMCwgImZpdCI6ICJpbnNpZGUifX19',
        'https://d2w8kbdekdi1gv.cloudfront.net/eyJidWNrZXQiOiAiYXJ0ZXJhLWltYWdlcy1idWNrZXQiLCAia2V5IjogImFydHdvcmtzLzY4NDAxNzg4LWFlZDAtNGFjNS05ODE0LWViOTkwM2JkYTgwZi82ODQwMTc4OC1hZWQwLTRhYzUtOTgxNC1lYjk5MDNiZGE4MGZfZnVsbC5qcGciLCAiZWRpdHMiOiB7InJlc2l6ZSI6IHsid2lkdGgiOiAxOTIwLCAiaGVpZ2h0IjogMTkyMCwgImZpdCI6ICJpbnNpZGUifX19',
        'https://d2w8kbdekdi1gv.cloudfront.net/eyJidWNrZXQiOiAiYXJ0ZXJhLWltYWdlcy1idWNrZXQiLCAia2V5IjogImFydHdvcmtzLzgxOGVkMTM1LThmOWEtNDA1Mi1hZjkwLWRhNjQxODVhYzNjMy84MThlZDEzNS04ZjlhLTQwNTItYWY5MC1kYTY0MTg1YWMzYzNfZnVsbC5qcGciLCAiZWRpdHMiOiB7InJlc2l6ZSI6IHsid2lkdGgiOiAxOTIwLCAiaGVpZ2h0IjogMTkyMCwgImZpdCI6ICJpbnNpZGUifX19'
    ]

    random_profile_images = [
        'https://d2w8kbdekdi1gv.cloudfront.net/eyJidWNrZXQiOiAiYXJ0ZXJhLWltYWdlcy1idWNrZXQiLCAia2V5IjogInByb2ZpbGVzLzQwZDEwNWRmLTYxMWUtNDNlMS1hZDk5LWM2NTRkYmJjMjg4Ny80MGQxMDVkZi02MTFlLTQzZTEtYWQ5OS1jNjU0ZGJiYzI4ODdfcHJvZmlsZV9waWN0dXJlLmpwZyIsICJ2ZXJzaW9uSWQiOiBudWxsLCAiZWRpdHMiOiB7InJlc2l6ZSI6IHsid2lkdGgiOiAzMjAsICJoZWlnaHQiOiAzMjAsICJmaXQiOiAiaW5zaWRlIn19fQ==',
        'https://d2w8kbdekdi1gv.cloudfront.net/eyJidWNrZXQiOiAiYXJ0ZXJhLWltYWdlcy1idWNrZXQiLCAia2V5IjogInByb2ZpbGVzL2IwYTQ2YjY4LTczMzYtNDcyYy05NTcxLTk3NWE0ODgyMDkyZC9iMGE0NmI2OC03MzM2LTQ3MmMtOTU3MS05NzVhNDg4MjA5MmRfcHJvZmlsZV9waWN0dXJlLmpwZyIsICJ2ZXJzaW9uSWQiOiBudWxsLCAiZWRpdHMiOiB7InJlc2l6ZSI6IHsid2lkdGgiOiAzMjAsICJoZWlnaHQiOiAzMjAsICJmaXQiOiAiaW5zaWRlIn19fQ==',
        'https://d2w8kbdekdi1gv.cloudfront.net/eyJidWNrZXQiOiAiYXJ0ZXJhLWltYWdlcy1idWNrZXQiLCAia2V5IjogInByb2ZpbGVzLzE5OGMxNzMxLWJkNGUtNDI4MC1hMjgyLTJkYTJlMTFhYmRjZC8xOThjMTczMS1iZDRlLTQyODAtYTI4Mi0yZGEyZTExYWJkY2RfcHJvZmlsZV9waWN0dXJlLmpwZyIsICJ2ZXJzaW9uSWQiOiBudWxsLCAiZWRpdHMiOiB7InJlc2l6ZSI6IHsid2lkdGgiOiAzMjAsICJoZWlnaHQiOiAzMjAsICJmaXQiOiAiaW5zaWRlIn19fQ==',
        'https://d2w8kbdekdi1gv.cloudfront.net/eyJidWNrZXQiOiAiYXJ0ZXJhLWltYWdlcy1idWNrZXQiLCAia2V5IjogInByb2ZpbGVzLzlmNWQwYzc4LWRlZTYtNDA3Yi04NzA3LWY0NjFkOGMzMTBkZS85ZjVkMGM3OC1kZWU2LTQwN2ItODcwNy1mNDYxZDhjMzEwZGVfcHJvZmlsZV9waWN0dXJlLmpwZyIsICJ2ZXJzaW9uSWQiOiBudWxsLCAiZWRpdHMiOiB7InJlc2l6ZSI6IHsid2lkdGgiOiAzMjAsICJoZWlnaHQiOiAzMjAsICJmaXQiOiAiaW5zaWRlIn19fQ==',
        'https://d2w8kbdekdi1gv.cloudfront.net/eyJidWNrZXQiOiAiYXJ0ZXJhLWltYWdlcy1idWNrZXQiLCAia2V5IjogInByb2ZpbGVzLzc3MzExZjYzLWRmZDAtNGJkOC04OTIwLWUwNjU1M2RiM2Y2Yy83NzMxMWY2My1kZmQwLTRiZDgtODkyMC1lMDY1NTNkYjNmNmNfcHJvZmlsZV9waWN0dXJlLmpwZyIsICJ2ZXJzaW9uSWQiOiBudWxsLCAiZWRpdHMiOiB7InJlc2l6ZSI6IHsid2lkdGgiOiAzMjAsICJoZWlnaHQiOiAzMjAsICJmaXQiOiAiaW5zaWRlIn19fQ==',
        'https://d2w8kbdekdi1gv.cloudfront.net/eyJidWNrZXQiOiAiYXJ0ZXJhLWltYWdlcy1idWNrZXQiLCAia2V5IjogInByb2ZpbGVzLzBkYTQ4YmEyLTViODktNGIyNC1hODJkLWY5YTUyNmM0NDliNC8wZGE0OGJhMi01Yjg5LTRiMjQtYTgyZC1mOWE1MjZjNDQ5YjRfcHJvZmlsZV9waWN0dXJlLmpwZyIsICJ2ZXJzaW9uSWQiOiBudWxsLCAiZWRpdHMiOiB7InJlc2l6ZSI6IHsid2lkdGgiOiAzMjAsICJoZWlnaHQiOiAzMjAsICJmaXQiOiAiaW5zaWRlIn19fQ==',
        'https://d2w8kbdekdi1gv.cloudfront.net/eyJidWNrZXQiOiAiYXJ0ZXJhLWltYWdlcy1idWNrZXQiLCAia2V5IjogInByb2ZpbGVzLzZhM2ZhOTljLTA4MzAtNDU3MS04MGVlLTMzZTRhZDc4ZWExZC82YTNmYTk5Yy0wODMwLTQ1NzEtODBlZS0zM2U0YWQ3OGVhMWRfcHJvZmlsZV9waWN0dXJlLnBuZyIsICJ2ZXJzaW9uSWQiOiAiNmNlNFNmU25DeTg0WHF1eWlWMDdaeExnUDBoTm85NnkiLCAiZWRpdHMiOiB7InJlc2l6ZSI6IHsid2lkdGgiOiA3MjIsICJoZWlnaHQiOiA1NTksICJmaXQiOiAiaW5zaWRlIn19fQ==',
        'https://d2w8kbdekdi1gv.cloudfront.net/eyJidWNrZXQiOiAiYXJ0ZXJhLWltYWdlcy1idWNrZXQiLCAia2V5IjogInByb2ZpbGVzLzAxZjU4NTBkLWE1YjYtNDIxYS04MWI1LTc0YmQ5MDJiYjYxOS8wMWY1ODUwZC1hNWI2LTQyMWEtODFiNS03NGJkOTAyYmI2MTlfcHJvZmlsZV9waWN0dXJlLmpwZyIsICJ2ZXJzaW9uSWQiOiAia1ZjMEdRdndmRkhiallKcmxTR3dLdHRzMnJueV9VTzQiLCAiZWRpdHMiOiB7InJlc2l6ZSI6IHsid2lkdGgiOiAzMDUsICJoZWlnaHQiOiA1MDAsICJmaXQiOiAiaW5zaWRlIn19fQ==',
        'https://d2w8kbdekdi1gv.cloudfront.net/eyJidWNrZXQiOiAiYXJ0ZXJhLWltYWdlcy1idWNrZXQiLCAia2V5IjogInByb2ZpbGVzL2Q2ZjIwZDI1LWViMTUtNDIxZS04ZGM0LWFkNmIwZjMwNDRhNC9kNmYyMGQyNS1lYjE1LTQyMWUtOGRjNC1hZDZiMGYzMDQ0YTRfcHJvZmlsZV9waWN0dXJlLmpwZyIsICJ2ZXJzaW9uSWQiOiBudWxsLCAiZWRpdHMiOiB7InJlc2l6ZSI6IHsid2lkdGgiOiAzMjAsICJoZWlnaHQiOiAzMjAsICJmaXQiOiAiaW5zaWRlIn19fQ==',
        'https://d2w8kbdekdi1gv.cloudfront.net/eyJidWNrZXQiOiAiYXJ0ZXJhLWltYWdlcy1idWNrZXQiLCAia2V5IjogInByb2ZpbGVzL2U5NmYyOTg3LTU5NzgtNDBhNC1iYjQ0LTU3NWM0OGQzMzJlNC9lOTZmMjk4Ny01OTc4LTQwYTQtYmI0NC01NzVjNDhkMzMyZTRfcHJvZmlsZV9waWN0dXJlLmpwZyIsICJ2ZXJzaW9uSWQiOiBudWxsLCAiZWRpdHMiOiB7InJlc2l6ZSI6IHsid2lkdGgiOiAzMjAsICJoZWlnaHQiOiAzMjAsICJmaXQiOiAiaW5zaWRlIn19fQ==',
        'https://d2w8kbdekdi1gv.cloudfront.net/eyJidWNrZXQiOiAiYXJ0ZXJhLWltYWdlcy1idWNrZXQiLCAia2V5IjogInByb2ZpbGVzL2RkYzZjYjI3LWNjNjQtNGU1Mi1hNjA0LWViYmNmYTJhMTY5ZC9kZGM2Y2IyNy1jYzY0LTRlNTItYTYwNC1lYmJjZmEyYTE2OWRfcHJvZmlsZV9waWN0dXJlLmpwZyIsICJ2ZXJzaW9uSWQiOiAiVVNHdTM5T1lZSzlXSTRvbWR3cGkwajlkVFh2NnFvd3ciLCAiZWRpdHMiOiB7InJlc2l6ZSI6IHsid2lkdGgiOiA1MDAsICJoZWlnaHQiOiA1MDAsICJmaXQiOiAiaW5zaWRlIn19fQ==',
        'https://d2w8kbdekdi1gv.cloudfront.net/eyJidWNrZXQiOiAiYXJ0ZXJhLWltYWdlcy1idWNrZXQiLCAia2V5IjogInByb2ZpbGVzL2IxM2JmNTllLThmNjUtNDYxYS1iZWJlLTA0N2M5ODQ0ZmYwMC9iMTNiZjU5ZS04ZjY1LTQ2MWEtYmViZS0wNDdjOTg0NGZmMDBfcHJvZmlsZV9waWN0dXJlLmpwZyIsICJ2ZXJzaW9uSWQiOiAiQmtuWThrODdJUkN0TTE4RDRFcHpOWnF2YkJoSlJJYWciLCAiZWRpdHMiOiB7InJlc2l6ZSI6IHsid2lkdGgiOiAzNzYsICJoZWlnaHQiOiA1MDAsICJmaXQiOiAiaW5zaWRlIn19fQ==',
        'https://d2w8kbdekdi1gv.cloudfront.net/eyJidWNrZXQiOiAiYXJ0ZXJhLWltYWdlcy1idWNrZXQiLCAia2V5IjogInByb2ZpbGVzL2U4ODFmOTE5LTYwZTgtNDU5Ni04MDZhLWJkYjY0MzQxY2JkZS9lODgxZjkxOS02MGU4LTQ1OTYtODA2YS1iZGI2NDM0MWNiZGVfcHJvZmlsZV9waWN0dXJlLmpwZyIsICJ2ZXJzaW9uSWQiOiAiTG83TU1xUEJfYTQzUS5jRElaZzVzVWcyZVJ4MWdNdTYiLCAiZWRpdHMiOiB7InJlc2l6ZSI6IHsid2lkdGgiOiA1MDAsICJoZWlnaHQiOiA1MDAsICJmaXQiOiAiaW5zaWRlIn19fQ==',
        'https://d2w8kbdekdi1gv.cloudfront.net/eyJidWNrZXQiOiAiYXJ0ZXJhLWltYWdlcy1idWNrZXQiLCAia2V5IjogInByb2ZpbGVzL2Y0MWM0Njg1LTM0YzEtNDYxYi1hMGEzLWQ4NzY2ZTJlY2U5My9mNDFjNDY4NS0zNGMxLTQ2MWItYTBhMy1kODc2NmUyZWNlOTNfcHJvZmlsZV9waWN0dXJlLmpwZyIsICJ2ZXJzaW9uSWQiOiAidFBPZHVwQ2o1NDhrUFU1R3YxcVpZclNQSWdGSlRQUzMiLCAiZWRpdHMiOiB7InJlc2l6ZSI6IHsid2lkdGgiOiA1MDAsICJoZWlnaHQiOiA1MDAsICJmaXQiOiAiaW5zaWRlIn19fQ==',
        'https://d2w8kbdekdi1gv.cloudfront.net/eyJidWNrZXQiOiAiYXJ0ZXJhLWltYWdlcy1idWNrZXQiLCAia2V5IjogInByb2ZpbGVzL2E2ZjIzMDdiLWI2Y2UtNGQyZC05YTc4LTAxZTRkMTM1M2MyMi9hNmYyMzA3Yi1iNmNlLTRkMmQtOWE3OC0wMWU0ZDEzNTNjMjJfcHJvZmlsZV9waWN0dXJlLmpwZyIsICJ2ZXJzaW9uSWQiOiBudWxsLCAiZWRpdHMiOiB7InJlc2l6ZSI6IHsid2lkdGgiOiAzMjAsICJoZWlnaHQiOiAzMjAsICJmaXQiOiAiaW5zaWRlIn19fQ=='
    ]

    def handle(self, *args, **kwargs):
        # Clear existing data to avoid duplication
        Artworks.objects.all().delete()
        Profiles.objects.all().delete()
        User.objects.all().delete()
        
        available_handles = self.handles.copy() 

        for i in range(15):
            # Check or create a random user
            username = f"user{i}"
            selected_profile_picture = random.choice(self.random_profile_images)
            user, created = User.objects.get_or_create(
                username=username,
                defaults={
                    "email": f"{username}@example.com",
                    "password": "password123"
                }
            )

            if not created:
                # Skip if the user already exists
                self.stdout.write(self.style.WARNING(f"User '{username}' already exists, skipping."))
                continue

            # Generate unique profile handle and image
            profile_handle = available_handles.pop(0)
            selected_profile_picture = random.choice(self.random_profile_images)

            # Create profile
            profile = Profiles.objects.create(
                user=user,
                profile_handle=profile_handle,
                profile_picture={
                    "main_1920": selected_profile_picture,
                    "main_600": selected_profile_picture,
                    "main_300": selected_profile_picture,
                    "source": selected_profile_picture
                }
            )

            # Generate random artwork data
            artwork_name = random.choice(self.titles)
            artwork_description = random.choice(self.descriptions)
            selected_images = random.choice(self.random_images)
            artwork_images = {
                "main_1920": selected_images,
                "main_600": selected_images,
                "main_300": selected_images,
                "source": selected_images
            }

            # Create artwork
            artwork = Artworks.objects.create(
                artwork_id=uuid.uuid4(),
                artwork_type="digital",  # Set according to your ArtworkTypeChoices
                artwork_privacy="public",  # Set according to your ArtworkPrivacyChoices
                artwork_name=artwork_name,
                artwork_date=timezone.now(),
                artwork_images=artwork_images,
                artwork_location="Random City",
                artwork_description=artwork_description,
                artwork_likes_counter=random.randint(0, 5000),
                artwork_comments_counter=random.randint(0, 5000),
                artwork_views_counter=random.randint(0, 50000),
                artwork_collections_counter=random.randint(0, 200),
                artwork_shares_counter=random.randint(0, 1000),
                artwork_main_image_height=random.choice([1920, 1080, 600]),
                artwork_main_image_width=random.choice([1920, 1080, 600]),
                profile=profile
            )

            # Output success message
            self.stdout.write(self.style.SUCCESS(f"Created artwork '{artwork_name}' with profile '{profile_handle}'"))

        self.stdout.write(self.style.SUCCESS("Database seeded with random artworks and profiles!"))