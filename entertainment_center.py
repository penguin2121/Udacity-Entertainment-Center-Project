# These lines import modules
import media  # This module includes the Movie class
import fresh_tomatoes

# Define a movie instance by 1) title, 2) storyline,
# 3) URL for poster image, 4) URL for trailer

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg"  # NOQA
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet.",
                     "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",  # NOQA
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

first_contact = media.Movie("Star Trek: First Contact",
                            "The crew of the enterprise travels back in time.",
                            "http://t2.gstatic.com/images?q=tbn:ANd9GcQqKE15EvuPYXqFa5X1PWPlljp1pu5Ss1UUNS98qp8RkJnSBSUU",  # NOQA
                            "https://www.youtube.com/watch?v=YQ1eiEvefKI")

logan = media.Movie("Logan",
                    "Wolverine as an old man.",
                    "http://t1.gstatic.com/images?q=tbn:ANd9GcRPoMqL1vglrh7OF_69pT8gYMYnYaq1r7WfPMcD587V9uOR_hW2",  # NOQA
                    "https://www.youtube.com/watch?v=f7kIl-Q1yrA")

ratatouille = media.Movie("Ratatouille",
                          "A cute rate goes on a journey",
                          "http://www.gstatic.com/tv/thumb/dvdboxart/165058/p165058_d_v8_aa.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=uVeNEbh3A4U")

ghost_busters = media.Movie("Ghost Busters (Original)",
                            "Stupid people fight ghosts.",
                            "http://t3.gstatic.com/images?q=tbn:ANd9GcRJG5IBNzP5r0lNiVbjvc-V4ejuqDRWorvC9cAx8eBYQ4hb5eVY",  # NOQA
                            "https://www.youtube.com/watch?v=eowrFdpcRbs")

movies = [toy_story, avatar, first_contact, logan, ratatouille, ghost_busters]
fresh_tomatoes.open_movies_page(movies) # Create movie page based on list of movie instances
