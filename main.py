from Usuario import Usuario

u1 = Usuario("Jorge", "Espino")
u2 = Usuario("Kevin", "Rodriguez")
u3 = Usuario("Richard", "Monzón")

u1.hacer_deposito(500).mostrar_balance_usuario().transfer_dinero(u2, 200).mostrar_balance_usuario()
u2.mostrar_balance_usuario()

