REGLAS = [
    # Facultad de Ciencias de la Salud
    {
        'if': ['empatia', 'servicio', 'analisis_cientifico', 'detalle'],
        'then': ['facultad_ciencias_salud']
    },
    {
        'if': ['paciencia', 'detalle', 'analisis_cientifico'],
        'then': ['facultad_ciencias_salud']
    },

    # Facultad de Ciencias Humanísticas
    {
        'if': ['cultura', 'dialogo', 'comunicacion', 'pensamiento_critico'],
        'then': ['facultad_ciencias_humanisticas']
    },
    {
        'if': ['creatividad', 'cultura', 'comunicacion'],
        'then': ['facultad_ciencias_humanisticas']
    },

    # Facultad de Enfermería
    {
        'if': ['empatia', 'paciencia', 'destreza_manual', 'trabajo_equipo'],
        'then': ['facultad_enfermeria']
    },
    {
        'if': ['servicio', 'detalle', 'trabajo_equipo'],
        'then': ['facultad_enfermeria']
    },

    # Facultad de Tecnología e Innovación
    {
        'if': ['tecnologia', 'innovacion', 'logica', 'matematicas'],
        'then': ['facultad_tecnologia_innovacion']
    },
    {
        'if': ['logica', 'creatividad', 'tecnologia'],
        'then': ['facultad_tecnologia_innovacion']
    },

    # Facultad de Ciencias Económicas
    {
        'if': ['negocios', 'planificacion', 'matematicas', 'estrategia'],
        'then': ['facultad_ciencias_economicas']
    },
    {
        'if': ['competitividad', 'negociacion', 'matematicas'],
        'then': ['facultad_ciencias_economicas']
    }
]

# Aptitudes y actitudes posibles = APAC
APAC_POSIBLES = [
    # Actitudes
    'empatia', 'servicio', 'paciencia', 'cultura', 'dialogo', 'creatividad',
    'tecnologia', 'innovacion', 'negocios', 'planificacion', 'competitividad',

    # Aptitudes
    'analisis_cientifico', 'detalle', 'comunicacion', 'pensamiento_critico',
    'destreza_manual', 'trabajo_equipo', 'logica', 'matematicas', 'negociacion', 'estrategia'
]
