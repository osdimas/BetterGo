import memory

# Implement more patterns to keep cheat as long updated as possible.
# Some of the patterns are disabled until we use them. It saves time while launching app.
# https://github.com/frk1/hazedumper/blob/master/config.json

try:
    dwGlowObjectManager = memory.get_sig('client.dll', rb'\xA1....\xA8\x01\x75\x4B', 4, 1)
    m_bDormant = memory.get_sig('client.dll', rb'\x8A\x81....\xC3\x32\xC0', 8, 2, False)
    # anim_overlays = memory.get_sig('client.dll', rb'\x8B\x89....\x8D\x0C\xD1', 0, 2, False)
    # clientstate_delta_ticks = memory.get_sig('engine.dll', rb'\xC7\x87........\xFF\x15....\x83\xC4\x08', 0, 2, False)
    # clientstate_choked_commands = memory.get_sig('engine.dll', rb'\x8B\x87....\x41', 0, 2, False)
    # clientstate_last_outgoing_command = memory.get_sig('engine.dll', rb'\x8B\x8F....\x8B\x87....\x41', 0, 2, False)
    # clientstate_net_channel = memory.get_sig('engine.dll', rb'\x8B\x8F....\x8B\x01\x8B\x40\x18', 0, 2, False)
    # convar_name_hash_table = memory.get_sig('vstdlib.dll', rb'\x8B\x3C\x85', 0, 3)
    dwForceAttack = memory.get_sig('client.dll', rb'\x89\x0D....\x8B\x0D....\x8B\xF2\x8B\xC1\x83\xCE\x04', 0, 2)
    dwForceAttack2 = memory.get_sig('client.dll', rb'\x89\x0D....\x8B\x0D....\x8B\xF2\x8B\xC1\x83\xCE\x04', 12, 2)
    dwForceJump = memory.get_sig('client.dll', rb'\x8B\x0D....\x8B\xD6\x8B\xC1\x83\xCA\x02', 0, 2)
    dwForceLeft = memory.get_sig('client.dll', rb'\x55\x8B\xEC\x51\x53\x8A\x5D\x08', 0, 465)
    dwForceRight = memory.get_sig('client.dll', rb'\x55\x8B\xEC\x51\x53\x8A\x5D\x08', 0, 512)
    dwClientState = memory.get_sig('engine.dll', rb'\xA1....\x33\xD2\x6A\x00\x6A\x00\x33\xC9\x89\xB0', 0, 1)
    dwClientState_GetLocalPlayer = memory.get_sig('engine.dll', rb'\x8B\x80....\x40\xC3', 0, 2, False)
    # dwClientState_IsHLTV = memory.get_sig('engine.dll', rb'\x80\xBF.....\x0F\x84....\x32\xDB', 0, 2, False)
    dwClientState_Map = memory.get_sig('engine.dll', rb'\x05....\xC3\xCC\xCC\xCC\xCC\xCC\xCC\xCC\xA1', 0, 1, False)
    dwClientState_MapDirectory = memory.get_sig('engine.dll', rb'\xB8....\xC3\x05....\xC3', 0, 7, False)
    dwClientState_MaxPlayer = memory.get_sig('engine.dll',
                                             rb'\xA1....\x8B\x80....\xC3\xCC\xCC\xCC\xCC\x55\x8B\xEC\x8A\x45\x08', 0, 7,
                                             False)
    dwClientState_PlayerInfo = memory.get_sig('engine.dll', rb'\x8B\x89....\x85\xC9\x0F\x84....\x8B\x01', 0, 2, False)
    dwClientState_State = memory.get_sig('engine.dll', rb'\x83\xB8.....\x0F\x94\xC0\xC3', 0, 2, False)
    dwClientState_ViewAngles = memory.get_sig('engine.dll',
                                              rb'\xF3\x0F\x11\x86....\xF3\x0F\x10\x44\x24.\xF3\x0F\x11\x86', 0, 4,
                                              False)
    dwEntityList = memory.get_sig('client.dll', rb'\xBB....\x83\xFF\x01\x0F\x8C....\x3B\xF8', 0, 1)
    # dwGameDir = memory.get_sig('engine.dll', rb'\x68....\x8D\x85....\x50\x68....\x68', 0, 1)
    # dwGameRulesProxy = memory.get_sig('client.dll', rb'\xA1....\x85\xC0\x0F\x84....\x80\xB8.....\x74\x7A', 0, 1)
    dwGlobalVars = memory.get_sig('engine.dll', rb'\x68....\x68....\xFF\x50\x08\x85\xC0', 0, 1)
    # dwInput = memory.get_sig('client.dll', rb'\xB9....\xF3\x0F\x11\x04\x24\xFF\x50\x10', 0, 1)
    dwLocalPlayer = memory.get_sig('client.dll', rb'\x8D\x34\x85....\x89\x15....\x8B\x41\x08\x8B\x48\x04\x83\xF9\xFF',
                                   4, 3)
    # dwMouseEnable = memory.get_sig('client.dll', rb'\xB9....\xFF\x50\x34\x85\xC0\x75\x10', 48, 1)
    # dwMouseEnablePtr = memory.get_sig('client.dll', rb'\xB9....\xFF\x50\x34\x85\xC0\x75\x10', 0, 1)
    dwPlayerResource = memory.get_sig('client.dll', rb'\x8B\x3D....\x85\xFF\x0F\x84....\x81\xC7', 0, 2)
    # dwRadarBase = memory.get_sig('client.dll', rb'\xA1....\x8B\x0C\xB0\x8B\x01\xFF\x50.\x46\x3B\x35....\x7C\xEA\x8B\x0D', 0, 1)
    # dwSensitivity = memory.get_sig('client.dll', rb'\x81\xF9....\x75\x1D\xF3\x0F\x10\x05....\xF3\x0F\x11\x44\x24.\x8B\x44\x24\x0C\x35....\x89\x44\x24\x0C', 44, 2)
    # dwSensitivityPtr = memory.get_sig('client.dll', rb'\x81\xF9....\x75\x1D\xF3\x0F\x10\x05....\xF3\x0F\x11\x44\x24.\x8B\x44\x24\x0C\x35....\x89\x44\x24\x0C', 0, 2)
    dwViewMatrix = memory.get_sig('client.dll', rb'\x0F\x10\x05....\x8D\x85....\xB9', 176, 3)
    # dwWeaponTable = memory.get_sig('client.dll', rb'\xB9....\x6A\x00\xFF\x50\x08\xC3', 0, 1)
    # dwWeaponTableIndex = memory.get_sig('client.dll', rb'\x39\x86....\x74\x06\x89\x86....\x8B\x86', 0, 2, False)
    interface_engine_cvar = memory.get_sig('vstdlib.dll', rb'\x8B\x0D....\xC7\x05', 0, 2)
    is_c4_owner = 0x3C8110
    m_flSpawnTime = 0x103C0
    dwbSendPackets = memory.get_sig('engine.dll',
                                    rb'\xB3\x01\x8B\x01\x8B\x40\x10\xFF\xD0\x84\xC0\x74\x0F\x80\xBF.....\x0F\x84', 1, 0,
                                    False, True)
    Cmd_ExecuteCommand = memory.get_sig('engine.dll',
                                        rb'\x55\x8B\xEC\x8B\x0D....\x81\xF9....\x75\x0C\xA1....\x35....\xEB\x05\x8B\x01\xFF\x50\x34\x50',
                                        0, 0, False, True)
    # 55 8B EC 8B 0D ? ? ? ? 81 F9 ? ? ? ? 75 0C A1 ? ? ? ? 35 ? ? ? ? EB 05 8B 01 FF 50 34 50 
    # netvars
    cs_gamerules_data = 0x0
    m_ArmorValue = 0x117CC
    m_Collision = 0x320
    m_CollisionGroup = 0x474
    m_Local = 0x2FCC
    m_MoveType = 0x25C
    m_OriginalOwnerXuidHigh = 0x31D4
    m_OriginalOwnerXuidLow = 0x31D0
    m_SurvivalGameRuleDecisionTypes = 0x1328
    m_SurvivalRules = 0xD00
    m_aimPunchAngle = 0x303C
    m_aimPunchAngleVel = 0x3048
    m_angEyeAnglesX = 0x117D0
    m_angEyeAnglesY = 0x117D4
    m_bBombDefused = 0x29C0
    m_bBombPlanted = 0x9A5
    m_bBombTicking = 0x2990
    m_bFreezePeriod = 0x20
    m_bGunGameImmunity = 0x9990
    m_bHasDefuser = 0x117DC
    m_bHasHelmet = 0x117C0
    m_bInReload = 0x32B5
    m_bIsDefusing = 0x997C
    m_bIsQueuedMatchmaking = 0x74
    m_bIsScoped = 0x9974
    m_bIsValveDS = 0x7C
    m_bSpotted = 0x93D
    m_bSpottedByMask = 0x980
    m_bStartedArming = 0x3400
    m_bUseCustomAutoExposureMax = 0x9D9
    m_bUseCustomAutoExposureMin = 0x9D8
    m_bUseCustomBloomScale = 0x9DA
    m_clrRender = 0x70
    m_dwBoneMatrix = 0x26A8
    m_fAccuracyPenalty = 0x3340
    m_fFlags = 0x104
    m_flC4Blow = 0x29A0
    m_flCustomAutoExposureMax = 0x9E0
    m_flCustomAutoExposureMin = 0x9DC
    m_flCustomBloomScale = 0x9E4
    m_flDefuseCountDown = 0x29BC
    m_flDefuseLength = 0x29B8
    m_flFallbackWear = 0x31E0
    m_flFlashDuration = 0x10470
    m_flFlashMaxAlpha = 0x1046C
    m_flLastBoneSetupTime = 0x2928
    m_flLowerBodyYawTarget = 0x9ADC
    m_flNextAttack = 0x2D80
    m_flNextPrimaryAttack = 0x3248
    m_flSimulationTime = 0x268
    m_flTimerLength = 0x29A4
    m_hActiveWeapon = 0x2F08
    m_hBombDefuser = 0x29C4
    m_hMyWeapons = 0x2E08
    m_hObserverTarget = 0x339C
    m_hOwner = 0x29DC
    m_hOwnerEntity = 0x14C
    m_hViewModel = 0x3308
    m_iAccountID = 0x2FD8
    m_iClip1 = 0x3274
    m_iCompetitiveRanking = 0x1A84
    m_iCompetitiveWins = 0x1B88
    m_iCrosshairId = 0x11838
    m_iDefaultFOV = 0x333C
    m_iEntityQuality = 0x2FBC
    m_iFOV = 0x31F4
    m_iFOVStart = 0x31F8
    m_iGlowIndex = 0x10488
    m_iHealth = 0x100
    m_iItemDefinitionIndex = 0x2FBA
    m_iItemIDHigh = 0x2FD0
    m_iMostRecentModelBoneCounter = 0x2690
    m_iObserverMode = 0x3388
    m_iShotsFired = 0x103E0
    m_iState = 0x3268
    m_iTeamNum = 0xF4
    m_lifeState = 0x25F
    m_nBombSite = 0x2994
    m_nFallbackPaintKit = 0x31D8
    m_nFallbackSeed = 0x31DC
    m_nFallbackStatTrak = 0x31E4
    m_nForceBone = 0x268C
    m_nTickBase = 0x3440
    m_nViewModelIndex = 0x29D0
    m_rgflCoordinateFrame = 0x444
    m_szCustomName = 0x304C
    m_szLastPlaceName = 0x35C4
    m_thirdPersonViewAngles = 0x31E8
    m_vecOrigin = 0x138
    m_vecVelocity = 0x114
    m_vecViewOffset = 0x108
    m_viewPunchAngle = 0x3030
    m_zoomLevel = 0x33E0
except Exception as err:
    print(err)
