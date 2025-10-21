class UsuarioRS:
    def __init__(self, username): self.username = username; self.seguidores = set(
    ); self.siguiendo = set(); self.publicaciones = []
    def seguir(self, u): self.siguiendo.add(
        u.username); u.seguidores.add(self.username)

    def publicar(self, t): self.publicaciones.append(t); return t
