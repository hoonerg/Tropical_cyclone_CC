#install pacakages
library(ggmap)
library(ggplot2)
library(dplyr)

# Browse regional data
noaa <- "https://www.ncei.noaa.gov/data/international-best-track-archive-for-climate-stewardship-ibtracs/v04r00/access/csv/"
WP.basin = read.csv(paste(noaa, "ibtracs.WP.list.v04r00.csv", sep = ""), stringsAsFactors = FALSE)

# Delete info of variations
WP.basin <- WP.basin[-1,]

# Pasing data in tbl_df
WP.basin.df <- tbl_df(WP.basin)

# Season, Latitude, Logitude : string -> number
WMO_WIND : str -> num & not -> m/s

# Extract months from ISO_time
WP.df <- mutate(WP.basin.df,
                SEASON = as.numeric(SEASON), 
                LAT = as.numeric(gsub("^ ", "", LAT)), 
                LON = as.numeric(gsub("^ ", "", LON)), 
                WMO_WIND = as.numeric(gsub("^ ", "", WMO_WIND)) * 0.5144, 
                ISO_TIME = as.POSIXct(ISO_TIME, tz = "UTC"), 
                Month = factor(substr(ISO_TIME, 6,7), labels = c(month.name))
                )
# TC ID Generation
substorms <- WP.df %>% filter(SEASON %in% 1999:2010 & !(NAME == "NOT NAMED")) %>%
  mutate(ID = as.factor(paste(NAME, SEASON, sep = ".")))
# Google api key and map
register_google(key = '********************************')
map <- ggmap(get_googlemap(center = c(lon=145, lat=40), 
                           zoom=3, maptype="terrain",
                           color="bw", scale=2), extent="device")

# TC Path 1999 - 2010
map + geom_path(data = substorms,
            aes(x = LON, y = LAT, group = ID, color = WMO_WIND), 
            alpha = 0.5, size = 0.8) +
  
  labs(x = "", y = "", colour = "Wind \n(m/sec)", 
       title = "Typhoon Trajectories") + theme(panel.background = element_rect(fill = "gray10", colour = "gray30"), 
       axis.text.x = element_blank(), 
       axis.text.y = element_blank(), axis.ticks = element_blank(), 
       panel.grid.major = element_blank(), panel.grid.minor = element_blank()
       )
