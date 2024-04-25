from datetime import datetime
from logging import Logger

from discord import Client
from discord import GroupCall
from discord import GroupChannel
from discord import Guild
from discord import Member
from discord import Message
from discord import PrivateCall
from discord import RawMessageDeleteEvent
from discord import RawMessageUpdateEvent
from discord import RawReactionActionEvent
from discord import RawReactionClearEvent
from discord import Reaction
from discord import Relationship
from discord import User
from discord import VoiceState
from discord.abc import GuildChannel
from discord.abc import Messageable
from discord.abc import PrivateChannel


class SocialLoggerClient(Client):
    """
    A subclass of discord.Client that logs all social-related events to a file for later reconstruction.
    """

    def __init__(self, logger: Logger, **kwargs) -> None:
        super().__init__(**kwargs)
        self._event_logger = logger

    # Channels

    async def on_guild_channel_delete(self, channel: GuildChannel) -> None:
        """
        Log the deletion of a guild channel.
        """
        self._event_logger.info(f"Channel {repr(channel)} was deleted.")

    async def on_guild_channel_create(self, channel: GuildChannel) -> None:
        """
        Log the creation of a guild channel.
        """
        self._event_logger.info(f"Channel {repr(channel)} was created.")

    async def on_guild_channel_update(self, before: GuildChannel, after: GuildChannel) -> None:
        """
        Log the update of a guild channel.
        """
        self._event_logger.info(f"Channel {repr(before)} was updated to {repr(after)}.")

    async def on_guild_channel_pins_update(
        self, channel: GuildChannel, last_pin: Message | None
    ) -> None:
        """
        Log the update of a guild channel's pins.
        """
        self._event_logger.info(
            f"Channel {repr(channel)} pins were changed. The last pin is {repr(last_pin)}."
        )

    async def on_private_channel_delete(self, channel: PrivateChannel) -> None:
        """
        Log the deletion of a private channel.
        """
        self._event_logger.info(f"Channel {repr(channel)} was deleted.")

    async def on_private_channel_create(self, channel: PrivateChannel) -> None:
        """
        Log the creation of a private channel.
        """
        self._event_logger.info(f"Channel {repr(channel)} was created.")

    async def on_private_channel_update(
        self, before: PrivateChannel, after: PrivateChannel
    ) -> None:
        """
        Log the update of a private channel.
        """
        self._event_logger.info(f"Channel {repr(before)} was updated to {repr(after)}.")

    async def on_private_channel_pins_update(
        self, channel: PrivateChannel, last_pin: Message | None
    ) -> None:
        """
        Log the update of a private channel's pins.
        """
        self._event_logger.info(
            f"Channel {repr(channel)} pins were changed. The last pin is {last_pin}."
        )

    async def on_group_join(self, channel: GroupChannel, user: User) -> None:
        """
        Log the joining of a group.
        """
        self._event_logger.info(f"User {repr(user)} joined group {repr(channel)}.")

    async def on_group_remove(self, channel: GroupChannel, user: User) -> None:
        """
        Log the removal of a user from a group.
        """
        self._event_logger.info(f"User {repr(user)} was removed from group {repr(channel)}.")

    async def on_typing(self, channel: Messageable, user: User | Member, when: datetime) -> None:
        """
        Log a user typing in a channel.
        """
        self._event_logger.info(f"User {repr(user)} is typing in channel {repr(channel)} at {when}.")

    # Relationships

    async def on_relationship_add(self, relationship: Relationship) -> None:
        """
        Log the addition of a relationship.
        """
        self._event_logger.info(f"Relationship {relationship} was added.")

    async def on_relationship_remove(self, relationship: Relationship) -> None:
        """
        Log the removal of a relationship.
        """
        self._event_logger.info(f"Relationship {relationship} was removed.")

    async def on_relationship_update(self, before: Relationship, after: Relationship) -> None:
        """
        Log the update of a relationship.
        """
        self._event_logger.info(f"Relationship {repr(before)} was updated to {repr(after)}.")

    async def on_friend_suggestion_add(self, user: User) -> None:
        """
        Log the addition of a friend suggestion.
        """
        self._event_logger.info(f"User {repr(user)} was suggested as a friend.")

    async def on_friend_suggestion_remove(self, user: User) -> None:
        """
        Log the removal of a friend suggestion.
        """
        self._event_logger.info(f"User {repr(user)} was removed as a friend suggestion.")

    # Calls

    async def on_call_create(self, call: GroupCall | PrivateCall) -> None:
        """
        Log the creation of a call.
        """
        self._event_logger.info(f"Call {call} was created.")

    async def on_call_update(
        self, call: GroupCall | PrivateCall, before: GroupCall | PrivateCall
    ) -> None:
        """
        Log the update of a call.
        """
        self._event_logger.info(f"Call {call} was updated from {repr(before)}.")

    # Guilds (but only the important parts)

    async def on_guild_join(self, guild) -> None:
        """
        Log the joining of a guild.
        """
        self._event_logger.info(f"Joined guild {repr(guild)}.")

    async def on_guild_remove(self, guild) -> None:
        """
        Log the removal of a guild.
        """
        self._event_logger.info(f"Left guild {repr(guild)}.")

    # Members

    async def on_member_join(self, member: Member) -> None:
        """
        Log the joining of a member.
        """
        self._event_logger.info(f"Member {repr(member)} joined {member.guild}.")

    async def on_member_remove(self, member: Member) -> None:
        """
        Log the removal of a member.
        """
        self._event_logger.info(f"Member {repr(member)} left.")

    async def on_member_update(self, before: Member, after: Member) -> None:
        """
        Log the update of a member.
        """
        self._event_logger.info(f"Member {repr(before)} was updated to {repr(after)}.")

    async def on_user_update(self, before: User, after: User) -> None:
        """
        Log the update of a user.
        """
        self._event_logger.info(f"User {repr(before)} was updated to {repr(after)}.")

    async def on_member_ban(self, guild: Guild, user: User | Member) -> None:
        """
        Log the banning of a member.
        """
        self._event_logger.info(f"Member {repr(user)} was banned from guild {repr(guild)}.")

    async def on_member_unban(self, guild: Guild, user: User) -> None:
        """
        Log the unbanning of a member.
        """
        self._event_logger.info(f"Member {repr(user)} was unbanned from guild {repr(guild)}.")

    async def on_presence_update(
        self, before: Member | Relationship, after: Member | Relationship
    ) -> None:
        """
        Log the update of a presence.
        """
        self._event_logger.info(f"Presence {repr(before)} was updated to {repr(after)}.")

    # Messages

    async def on_message(self, message: Message) -> None:
        """
        Log the sending of a message.
        """
        self._event_logger.info(
            f'Message {repr(message)} was sent with content {message.content!r}.'
        )

    async def on_message_edit(self, before: Message, after: Message) -> None:
        """
        Log the editing of a message.
        """
        self._event_logger.info(
            f'Message {repr(before)} with content {before.content!r} was updated to {repr(after)} with content {after.content!r}.'
        )

    async def on_message_delete(self, message: Message) -> None:
        """
        Log the deletion of a message.
        """
        self._event_logger.info(
            f'Message {repr(message)} was deleted with content {message.content!r}.'
        )

    async def on_bulk_message_delete(self, messages: list[Message]) -> None:
        """
        Log the bulk deletion of messages.
        """
        self._event_logger.info(f"Messages {[repr(message) for message in messages]} were bulk deleted.")

    async def on_raw_message_edit(self, payload: RawMessageUpdateEvent) -> None:
        """
        Log the raw editing of a message.
        """
        channel = await self.fetch_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        self._event_logger.info(
            f'Message {repr(message)} was updated with content {message.content!r}.'
        )

    async def on_raw_message_delete(self, payload: RawMessageDeleteEvent) -> None:
        """
        Log the raw deletion of a message.
        """
        channel = await self.fetch_channel(payload.channel_id)
        self._event_logger.info(f"Message {payload.message_id} was deleted from {repr(channel)}.")

    # async def on_recent_mention_delete(self, message: Message) -> None:
    #     """
    #     Log the deletion of a recent mention.
    #     """
    #     self._event_logger.info(f"Message {repr(message)} was deleted.")
    #
    # async def on_raw_recent_mention_delete(self, message_id: int) -> None:
    #     """
    #     Log the raw deletion of a recent mention.
    #     """
    #     self._event_logger.info(f"Message {message_id} was deleted.")

    # Reactions

    async def on_reaction_add(self, reaction: Reaction, user: Member | User) -> None:
        """
        Log the addition of a reaction.
        """
        self._event_logger.info(f"Reaction {reaction} was added by {repr(user)}.")

    async def on_reaction_remove(self, reaction: Reaction, user: Member | User) -> None:
        """
        Log the removal of a reaction.
        """
        self._event_logger.info(f"Reaction {repr(reaction)} was removed by {repr(user)}.")

    async def on_reaction_clear(self, message: Message, reactions: list[Reaction]) -> None:
        """
        Log the clearing of reactions.
        """
        self._event_logger.info(f"Reactions {[repr(reaction) for reaction in reactions]} were cleared from message {repr(message)}.")

    async def on_reaction_clear_emoji(self, reaction: Reaction) -> None:
        """
        Log the clearing of a reaction by emoji.
        """
        self._event_logger.info(f"Reaction {repr(reaction)} was cleared.")

    async def on_raw_reaction_add(self, payload: RawReactionActionEvent) -> None:
        """
        Log the raw addition of a reaction.
        """
        self._event_logger.info(
            f"Reaction {payload.emoji} was added to message {payload.message_id}."
        )

    async def on_raw_reaction_clear(self, payload: RawReactionClearEvent) -> None:
        """
        Log the raw removal of a reaction.
        """
        self._event_logger.info(f"Reactions were cleared from message {payload.message_id}.")

    async def on_raw_reaction_clear_emoji(self, payload: RawReactionClearEvent) -> None:
        """
        Log the raw clearing of a reaction by emoji.
        """
        self._event_logger.info(f"A single reaction was cleared from message {payload.message_id}.")

    # Voice

    async def on_voice_state_update(
        self, member: Member, before: VoiceState, after: VoiceState
    ) -> None:
        """
        Log the update of a voice state.
        """
        self._event_logger.info(f"Voice state {repr(before)} was updated to {repr(after)} for {repr(member)}.")


__all__ = ("SocialLoggerClient",)
