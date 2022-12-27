from src.server.routers import type_of_play, performance, play, user, ticket, hall

routers = (
    type_of_play.router,
    performance.router,
    play.router,
    user.router,
    ticket.router,
    hall.router,
    )
