class GameStats():
    """游戏的统计信息"""
    def __init__(self, ai_settings):
        self.ai_settings=ai_settings
        self.reset_stats()
        #是否开始游戏
        self.game_action=False

        #最高得分
        self.high_score=0
        self.level=1#等级

    def reset_stats(self):
        """初始化统计信息"""
        self.ships_left=self.ai_settings.ship_limit
        self.score=0
        self.level=1