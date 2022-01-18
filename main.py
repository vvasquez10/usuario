from Usuario import Usuario

u1 = Usuario("Jorge", "Espino")
u2 = Usuario("Kevin", "Rodriguez")
u3 = Usuario("Richard", "Monzón")

u1.hacer_deposito(500)
u1.mostrar_balance_usuario()

u1.transfer_dinero(u2, 200)
u2.mostrar_balance_usuario()
u1.mostrar_balance_usuario()
