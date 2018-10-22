from channels.routing import ProtocolTypeRouter, URLRouter

from django.urls import path

from api.consumers import LeaderBoard, Portfolio,nifty_channel,graph_data_channel, ticker_data_channel, sell_channel

application = ProtocolTypeRouter({
		"websocket":URLRouter([
				path("leaderboard-channel/",LeaderBoard),
				path("portfolio-channel/",Portfolio),
				path("nifty-channel/",nifty_channel),
				path("graph-channel/",graph_data_channel),
				path("ticker-channel/",ticker_data_channel),
				path("sell-channel/",sell_channel),
			])

	})