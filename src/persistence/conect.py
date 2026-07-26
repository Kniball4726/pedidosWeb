import sqlite3

class Conectar:

    def __init__(self):
        try:
            # Crear y conectar base de datos
            self.conectar = sqlite3.connect("src/data/pedidos.db")
            
            if self.conectar:
                print("Conexion establecida con exito")
            else:
                print("No se puede conectar a la base de datos")
            
            # Se crea un cursor para ejecutar comandos sql
            
            cursor = self.conectar.cursor()

            # Se crean las bases de datos 
            cursor.executescript("""
                                
                CREATE TABLE IF NOT EXISTS roles (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                rol TEXT NOT NULL UNIQUE 
                                );

                CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        dni TEXT NOT NULL,
                        usuario TEXT NOT NULL UNIQUE,
                        clave TEXT NOT NULL,
                        email TEXT UNIQUE NOT NULL,
                        rol INTEGER NOT NULL,
                        FOREIGN KEY (rol) REFERENCES roles(id)
                        );
                
                

                CREATE TABLE IF NOT EXISTS logistica (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            logistica TEXT UNIQUE NOT NULL,
                            usuario TEXT NOT NULL,
                            FOREIGN KEY (usuario) REFERENCES usuarios(id)
                            ON DELETE CASCADE
                            );
                                
                CREATE TABLE IF NOT EXISTS clientes(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            cliente TEXT NOT NULL UNIQUE,
                            direccion TEXT,
                            cuil TEXT NOT NULL UNIQUE,
                            email TEXT UNIQUE NOT NULL,
                            telefono TEXT,
                            usuario TEXT NOT NULL,
                            FOREIGN KEY (usuario) REFERENCES usuarios(id)
                        );

                CREATE TABLE IF NOT EXISTS pedidos(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        fecha TEXT NOT NULL,
                        notapedido NUMERIC NOT NULL UNIQUE,
                        bultos INTEGER NOT NULL,
                        numeropedido INTEGER,
                        operario TEXT NOT NULL,
                        cliente TEXT NOT NULL,
                        
                        FOREIGN KEY (cliente) REFERENCES clientes(id),
                        FOREIGN KEY (operario) REFERENCES usuarios(id)
                        )
                        """)
            
            usuario=[("95777596", "Gregory", "1713", "glrd4726@gmail.com","Operario",),
                    ("95777596", "GregoryD", "1713", "glrd4726ml@gmail.com","Dev",)]

            roles = [("Admin",),("Operario",),("Dev",),("Lector",)]

            # Inserta toda la lista en una sola operación eficiente
            cursor.executemany("INSERT INTO usuarios (dni, usuario,clave,email,rol) VALUES (?,?,?,?,?)", usuario)
            cursor.executemany("INSERT INTO roles (rol) VALUES (?)", roles)


            self.conectar.commit()
            self.conectar.close()
        except KeyboardInterrupt:
            exit()
        except sqlite3.DatabaseError as e:
            print(f"Error en la base de datos {e}")
        except sqlite3.Error as e:
            print(f"Error en conexion a la base de datos {e}")
            