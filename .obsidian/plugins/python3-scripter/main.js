/*
THIS IS A GENERATED/BUNDLED FILE BY ESBUILD
if you want to view the source, please visit the github repository of this plugin
*/

var __create = Object.create;
var __defProp = Object.defineProperty;
var __getOwnPropDesc = Object.getOwnPropertyDescriptor;
var __getOwnPropNames = Object.getOwnPropertyNames;
var __getProtoOf = Object.getPrototypeOf;
var __hasOwnProp = Object.prototype.hasOwnProperty;
var __export = (target, all) => {
  for (var name in all)
    __defProp(target, name, { get: all[name], enumerable: true });
};
var __copyProps = (to, from, except, desc) => {
  if (from && typeof from === "object" || typeof from === "function") {
    for (let key of __getOwnPropNames(from))
      if (!__hasOwnProp.call(to, key) && key !== except)
        __defProp(to, key, { get: () => from[key], enumerable: !(desc = __getOwnPropDesc(from, key)) || desc.enumerable });
  }
  return to;
};
var __toESM = (mod, isNodeMode, target) => (target = mod != null ? __create(__getProtoOf(mod)) : {}, __copyProps(
  // If the importer is in node compatibility mode or this is not an ESM
  // file that has been converted to a CommonJS file using a Babel-
  // compatible transform (i.e. "__esModule" has not been set), then set
  // "default" to the CommonJS "module.exports" for node compatibility.
  isNodeMode || !mod || !mod.__esModule ? __defProp(target, "default", { value: mod, enumerable: true }) : target,
  mod
));
var __toCommonJS = (mod) => __copyProps(__defProp({}, "__esModule", { value: true }), mod);

// main.ts
var main_exports = {};
__export(main_exports, {
  default: () => PythonScripterPlugin
});
module.exports = __toCommonJS(main_exports);
var import_obsidian = require("obsidian");
var path = __toESM(require("path"));
var fs = __toESM(require("fs"));
var import_child_process = require("child_process");
var DEFAULT_SETTINGS = {
  pythonPath: ""
};
var PythonScripterPlugin = class extends import_obsidian.Plugin {
  getBasePath() {
    let basePath;
    if (this.app.vault.adapter instanceof import_obsidian.FileSystemAdapter) {
      basePath = this.app.vault.adapter.getBasePath();
    } else {
      throw new Error("Cannot determine base path.");
    }
    return `${basePath}`;
  }
  async onload() {
    await this.loadSettings();
    var basePath = this.getBasePath();
    var defaultRelativePath = path.join(".", this.app.vault.configDir, "scripts", "python");
    this.pythonDirectory = path.join(basePath, defaultRelativePath);
    this.pythonDirectoryRelative = defaultRelativePath;
    if (this.settings.pythonPath != "") {
      this.pythonDirectory = path.join(basePath, this.settings.pythonPath);
      this.pythonDirectoryRelative = this.settings.pythonPath;
    } else {
      this.pythonDirectory = path.join(basePath, defaultRelativePath);
      this.pythonDirectoryRelative = defaultRelativePath;
    }
    console.log(this.pythonDirectoryRelative);
    try {
      await this.app.vault.createFolder(this.pythonDirectoryRelative);
    } catch (error) {
    }
    var files = fs.readdirSync(this.pythonDirectory);
    for (var index = 0; index < files.length; index++) {
      const filePath = path.join(this.pythonDirectory, files[index]);
      const fileName = files[index];
      const basePath2 = this.getBasePath();
      const obsidianCommand = {
        id: "run-" + files[index],
        name: "Run " + files[index],
        callback: () => {
          fs.stat(filePath, (err, stats) => {
            var _a, _b, _c, _d;
            if (err) {
              console.error(err);
              return;
            }
            if (stats.isFile()) {
              var local_current_file_path = (_b = (_a = this.app.workspace.activeEditor) == null ? void 0 : _a.file) == null ? void 0 : _b.path;
              if (local_current_file_path === void 0) {
                local_current_file_path = "";
              }
              (0, import_child_process.exec)(`python3 ${filePath} ${basePath2} "${local_current_file_path}"`, { cwd: this.pythonDirectory }, (error, stdout, stderr) => {
                if (error) {
                  new import_obsidian.Notice(`Error executing script ${filePath}: ${error}`);
                  return;
                }
                new import_obsidian.Notice(`Script ` + fileName + ` output:
${stdout}`);
              });
            } else if (stats.isDirectory()) {
              var dir = path.join(filePath);
              var executable = path.join(".", filePath, "src", "main.py");
              var local_current_file_path = (_d = (_c = this.app.workspace.activeEditor) == null ? void 0 : _c.file) == null ? void 0 : _d.path;
              if (local_current_file_path === void 0) {
                local_current_file_path = "";
              }
              (0, import_child_process.exec)(`python3 ${path.join(filePath, "src", "main.py")} ${basePath2} "${local_current_file_path}"`, { cwd: dir }, (error, stdout, stderr) => {
                if (error) {
                  new import_obsidian.Notice(`Error executing folder program: ${error}`);
                  return;
                }
                new import_obsidian.Notice(`Script ` + fileName + " " + basePath2 + ` output:
${stdout}`);
              });
            }
          });
        }
      };
      this.addCommand(obsidianCommand);
    }
    this.addSettingTab(new PythonScripterSettingTab(this.app, this));
  }
  onunload() {
  }
  async loadSettings() {
    this.settings = Object.assign({}, DEFAULT_SETTINGS, await this.loadData());
  }
  async saveSettings() {
    await this.saveData(this.settings);
  }
};
var PythonScripterSettingTab = class extends import_obsidian.PluginSettingTab {
  constructor(app, plugin) {
    super(app, plugin);
    this.plugin = plugin;
  }
  display() {
    const { containerEl } = this;
    containerEl.empty();
    new import_obsidian.Setting(containerEl).setName("Python Script Path").setDesc("Defaults to .obsidian\\scripts\\python").addText((text) => text.setPlaceholder("Enter path").setValue(this.plugin.settings.pythonPath).onChange(async (value) => {
      this.plugin.settings.pythonPath = value;
      await this.plugin.saveSettings();
    }));
  }
};
//# sourceMappingURL=data:application/json;base64,ewogICJ2ZXJzaW9uIjogMywKICAic291cmNlcyI6IFsibWFpbi50cyJdLAogICJzb3VyY2VzQ29udGVudCI6IFsiaW1wb3J0IHsgQXBwLCBFZGl0b3IsIEZpbGVTeXN0ZW1BZGFwdGVyLCBNYXJrZG93blZpZXcsIE1vZGFsLCBOb3RpY2UsIFBsdWdpbiwgUGx1Z2luU2V0dGluZ1RhYiwgU2V0dGluZyB9IGZyb20gJ29ic2lkaWFuJztcclxuaW1wb3J0ICogYXMgcGF0aCBmcm9tICdwYXRoJztcclxuaW1wb3J0ICogYXMgZnMgZnJvbSAnZnMnO1xyXG5pbXBvcnQgeyBleGVjIH0gZnJvbSAnY2hpbGRfcHJvY2Vzcyc7XHJcblxyXG5cclxuaW50ZXJmYWNlIFB5dGhvblNjcmlwdGVyU2V0dGluZ3Mge1xyXG5cdHB5dGhvblBhdGg6IHN0cmluZztcclxufVxyXG5cclxuY29uc3QgREVGQVVMVF9TRVRUSU5HUzogUHl0aG9uU2NyaXB0ZXJTZXR0aW5ncyA9IHtcclxuXHRweXRob25QYXRoOiBcIlwiXHJcbn1cclxuXHJcbmV4cG9ydCBkZWZhdWx0IGNsYXNzIFB5dGhvblNjcmlwdGVyUGx1Z2luIGV4dGVuZHMgUGx1Z2luIHtcclxuXHRzZXR0aW5nczogUHl0aG9uU2NyaXB0ZXJTZXR0aW5ncztcclxuXHRweXRob25EaXJlY3Rvcnk6IHN0cmluZztcclxuXHRweXRob25EaXJlY3RvcnlSZWxhdGl2ZTogc3RyaW5nO1xyXG5cclxuXHRnZXRCYXNlUGF0aCgpOiBzdHJpbmcge1xyXG4gICAgICAgIGxldCBiYXNlUGF0aDtcclxuICAgICAgICAvLyBiYXNlIHBhdGhcclxuICAgICAgICBpZiAodGhpcy5hcHAudmF1bHQuYWRhcHRlciBpbnN0YW5jZW9mIEZpbGVTeXN0ZW1BZGFwdGVyKSB7XHJcbiAgICAgICAgICAgIGJhc2VQYXRoID0gdGhpcy5hcHAudmF1bHQuYWRhcHRlci5nZXRCYXNlUGF0aCgpO1xyXG4gICAgICAgIH0gZWxzZSB7XHJcbiAgICAgICAgICAgIHRocm93IG5ldyBFcnJvcignQ2Fubm90IGRldGVybWluZSBiYXNlIHBhdGguJyk7XHJcbiAgICAgICAgfVxyXG4gICAgICAgIHJldHVybiBgJHtiYXNlUGF0aH1gO1xyXG4gICAgfVxyXG5cclxuXHRhc3luYyBvbmxvYWQoKSB7XHJcblx0XHRhd2FpdCB0aGlzLmxvYWRTZXR0aW5ncygpO1xyXG5cdFx0dmFyIGJhc2VQYXRoID0gdGhpcy5nZXRCYXNlUGF0aCgpO1xyXG5cdFx0dmFyIGRlZmF1bHRSZWxhdGl2ZVBhdGg6IHN0cmluZyA9IHBhdGguam9pbihcIi5cIiwgdGhpcy5hcHAudmF1bHQuY29uZmlnRGlyLCBcInNjcmlwdHNcIiwgXCJweXRob25cIik7XHJcblx0XHR0aGlzLnB5dGhvbkRpcmVjdG9yeSA9IHBhdGguam9pbihiYXNlUGF0aCwgZGVmYXVsdFJlbGF0aXZlUGF0aCk7XHJcblx0XHR0aGlzLnB5dGhvbkRpcmVjdG9yeVJlbGF0aXZlID0gZGVmYXVsdFJlbGF0aXZlUGF0aFxyXG5cdFx0aWYgKHRoaXMuc2V0dGluZ3MucHl0aG9uUGF0aCAhPSBcIlwiKSB7XHJcblx0XHRcdHRoaXMucHl0aG9uRGlyZWN0b3J5ID0gcGF0aC5qb2luKGJhc2VQYXRoLCB0aGlzLnNldHRpbmdzLnB5dGhvblBhdGgpO1xyXG5cdFx0XHR0aGlzLnB5dGhvbkRpcmVjdG9yeVJlbGF0aXZlID0gdGhpcy5zZXR0aW5ncy5weXRob25QYXRoXHJcblx0XHR9IGVsc2Uge1xyXG5cdFx0XHR0aGlzLnB5dGhvbkRpcmVjdG9yeSA9IHBhdGguam9pbihiYXNlUGF0aCwgZGVmYXVsdFJlbGF0aXZlUGF0aCk7XHJcblx0XHRcdHRoaXMucHl0aG9uRGlyZWN0b3J5UmVsYXRpdmUgPSBkZWZhdWx0UmVsYXRpdmVQYXRoXHJcblx0XHR9XHJcblx0XHRjb25zb2xlLmxvZyh0aGlzLnB5dGhvbkRpcmVjdG9yeVJlbGF0aXZlKVxyXG5cdFx0dHJ5IHtcclxuXHRcdFx0YXdhaXQgdGhpcy5hcHAudmF1bHQuY3JlYXRlRm9sZGVyKHRoaXMucHl0aG9uRGlyZWN0b3J5UmVsYXRpdmUpO1xyXG5cdFx0XHQvL25ldyBOb3RpY2UodGhpcy5weXRob25EaXJlY3RvcnkgKyBcIiBjcmVhdGVkXCIpO1xyXG5cdFx0fSBjYXRjaCAoZXJyb3IpIHtcclxuXHRcdFx0Ly9uZXcgTm90aWNlKFwiRXJyb3IgY3JlYXRpbmcgXCIgKyB0aGlzLnB5dGhvbkRpcmVjdG9yeSk7XHJcblx0XHR9XHJcblxyXG5cdFx0dmFyIGZpbGVzOiBzdHJpbmdbXSA9IGZzLnJlYWRkaXJTeW5jKHRoaXMucHl0aG9uRGlyZWN0b3J5KTtcclxuXHRcdGZvciAodmFyIGluZGV4ID0gMDsgaW5kZXggPCBmaWxlcy5sZW5ndGg7IGluZGV4KyspIHtcclxuXHRcdFx0Y29uc3QgZmlsZVBhdGggPSBwYXRoLmpvaW4odGhpcy5weXRob25EaXJlY3RvcnksIGZpbGVzW2luZGV4XSk7XHJcblx0XHRcdGNvbnN0IGZpbGVOYW1lID0gZmlsZXNbaW5kZXhdO1xyXG5cdFx0XHRjb25zdCBiYXNlUGF0aCA9IHRoaXMuZ2V0QmFzZVBhdGgoKTtcclxuXHRcdFx0Y29uc3Qgb2JzaWRpYW5Db21tYW5kID0ge1xyXG5cdFx0XHRcdGlkOiBcInJ1bi1cIitmaWxlc1tpbmRleF0sXHJcblx0XHRcdFx0bmFtZTogJ1J1biAnK2ZpbGVzW2luZGV4XSxcclxuXHRcdFx0XHRjYWxsYmFjazogKCkgPT4ge1xyXG5cdFx0XHRcdFx0ZnMuc3RhdChmaWxlUGF0aCwgKGVycjogYW55LCBzdGF0czogeyBpc0ZpbGU6ICgpID0+IGFueTsgaXNEaXJlY3Rvcnk6ICgpID0+IGFueTsgfSkgPT4ge1xyXG5cdFx0XHRcdFx0XHRpZiAoZXJyKSB7XHJcblx0XHRcdFx0XHRcdCAgY29uc29sZS5lcnJvcihlcnIpO1xyXG5cdFx0XHRcdFx0XHQgIHJldHVybjtcclxuXHRcdFx0XHRcdFx0fVxyXG5cdFx0XHRcdFx0XHRpZiAoc3RhdHMuaXNGaWxlKCkpIHtcclxuXHRcdFx0XHRcdFx0XHR2YXIgIGxvY2FsX2N1cnJlbnRfZmlsZV9wYXRoID0gdGhpcy5hcHAud29ya3NwYWNlLmFjdGl2ZUVkaXRvcj8uZmlsZT8ucGF0aDtcclxuXHRcdFx0XHRcdFx0XHRpZiAobG9jYWxfY3VycmVudF9maWxlX3BhdGggPT09IHVuZGVmaW5lZCkge1xyXG5cdFx0XHRcdFx0XHRcdFx0bG9jYWxfY3VycmVudF9maWxlX3BhdGggPSBcIlwiO1xyXG5cdFx0XHRcdFx0XHRcdH1cclxuXHRcdFx0XHRcdFx0XHRleGVjKGBweXRob24gJHtmaWxlUGF0aH0gJHtiYXNlUGF0aH0gXFxcIiR7bG9jYWxfY3VycmVudF9maWxlX3BhdGh9XFxcImAsIHtjd2Q6IHRoaXMucHl0aG9uRGlyZWN0b3J5fSwgKGVycm9yOiBhbnksIHN0ZG91dDogYW55LCBzdGRlcnI6IGFueSkgPT4ge1xyXG5cdFx0XHRcdFx0XHRcdFx0aWYgKGVycm9yKSB7XHJcblx0XHRcdFx0XHRcdFx0XHRcdG5ldyBOb3RpY2UoYEVycm9yIGV4ZWN1dGluZyBzY3JpcHQgJHtmaWxlUGF0aH06ICR7ZXJyb3J9YCk7XHJcblx0XHRcdFx0XHRcdFx0XHRcdHJldHVybjtcclxuXHRcdFx0XHRcdFx0XHRcdH1cclxuXHRcdFx0XHRcdFx0XHRcdG5ldyBOb3RpY2UoYFNjcmlwdCBgICsgIGZpbGVOYW1lICsgYCBvdXRwdXQ6XFxuJHtzdGRvdXR9YCk7XHJcblx0XHRcdFx0XHRcdFx0fSk7XHJcblx0XHRcdFx0XHRcdH0gZWxzZSBpZiAoc3RhdHMuaXNEaXJlY3RvcnkoKSkgeyBcclxuXHRcdFx0XHRcdFx0XHR2YXIgZGlyID0gcGF0aC5qb2luKGZpbGVQYXRoKTtcclxuXHRcdFx0XHRcdFx0XHR2YXIgZXhlY3V0YWJsZSA9IHBhdGguam9pbihcIi5cIiwgZmlsZVBhdGgsIFwic3JjXCIsIFwibWFpbi5weVwiKTtcclxuXHRcdFx0XHRcdFx0XHR2YXIgIGxvY2FsX2N1cnJlbnRfZmlsZV9wYXRoID0gdGhpcy5hcHAud29ya3NwYWNlLmFjdGl2ZUVkaXRvcj8uZmlsZT8ucGF0aDtcclxuXHRcdFx0XHRcdFx0XHRpZiAobG9jYWxfY3VycmVudF9maWxlX3BhdGggPT09IHVuZGVmaW5lZCkge1xyXG5cdFx0XHRcdFx0XHRcdFx0bG9jYWxfY3VycmVudF9maWxlX3BhdGggPSBcIlwiO1xyXG5cdFx0XHRcdFx0XHRcdH1cclxuXHRcdFx0XHRcdFx0XHRleGVjKGBweXRob24gJHtwYXRoLmpvaW4oZmlsZVBhdGgsIFwic3JjXCIsIFwibWFpbi5weVwiKX0gJHtiYXNlUGF0aH0gXFxcIiR7bG9jYWxfY3VycmVudF9maWxlX3BhdGh9XFxcImAsIHtjd2Q6IGRpcn0sIChlcnJvcjogYW55LCBzdGRvdXQ6IGFueSwgc3RkZXJyOiBhbnkpID0+IHtcclxuXHRcdFx0XHRcdFx0XHRcdGlmIChlcnJvcikge1xyXG5cdFx0XHRcdFx0XHRcdFx0XHRuZXcgTm90aWNlKGBFcnJvciBleGVjdXRpbmcgZm9sZGVyIHByb2dyYW06ICR7ZXJyb3J9YCk7XHJcblx0XHRcdFx0XHRcdFx0XHRcdHJldHVybjtcclxuXHRcdFx0XHRcdFx0XHRcdH1cclxuXHRcdFx0XHRcdFx0XHRcdG5ldyBOb3RpY2UoYFNjcmlwdCBgICsgIGZpbGVOYW1lICsgXCIgXCIgKyBiYXNlUGF0aCArIGAgb3V0cHV0OlxcbiR7c3Rkb3V0fWApO1xyXG5cdFx0XHRcdFx0XHRcdH0pO1xyXG5cdFx0XHRcdFx0XHR9XHJcblx0XHRcdFx0XHQgIH0pO1xyXG5cdFx0XHRcdFxyXG5cdFx0XHRcdH1cclxuXHRcdFx0fVxyXG5cdFx0XHR0aGlzLmFkZENvbW1hbmQob2JzaWRpYW5Db21tYW5kKTtcclxuXHRcdH0gXHJcblxyXG5cdFx0Ly8gVGhpcyBhZGRzIGEgc2V0dGluZ3MgdGFiIHNvIHRoZSB1c2VyIGNhbiBjb25maWd1cmUgdmFyaW91cyBhc3BlY3RzIG9mIHRoZSBwbHVnaW5cclxuXHRcdHRoaXMuYWRkU2V0dGluZ1RhYihuZXcgUHl0aG9uU2NyaXB0ZXJTZXR0aW5nVGFiKHRoaXMuYXBwLCB0aGlzKSk7XHJcblxyXG5cdH1cclxuXHJcblx0b251bmxvYWQoKSB7XHJcblxyXG5cdH1cclxuXHJcblx0YXN5bmMgbG9hZFNldHRpbmdzKCkge1xyXG5cdFx0dGhpcy5zZXR0aW5ncyA9IE9iamVjdC5hc3NpZ24oe30sIERFRkFVTFRfU0VUVElOR1MsIGF3YWl0IHRoaXMubG9hZERhdGEoKSk7XHJcblx0fVxyXG5cclxuXHRhc3luYyBzYXZlU2V0dGluZ3MoKSB7XHJcblx0XHRhd2FpdCB0aGlzLnNhdmVEYXRhKHRoaXMuc2V0dGluZ3MpO1xyXG5cdH1cclxufVxyXG5cclxuY2xhc3MgUHl0aG9uU2NyaXB0ZXJTZXR0aW5nVGFiIGV4dGVuZHMgUGx1Z2luU2V0dGluZ1RhYiB7XHJcblx0cGx1Z2luOiBQeXRob25TY3JpcHRlclBsdWdpbjtcclxuXHJcblx0Y29uc3RydWN0b3IoYXBwOiBBcHAsIHBsdWdpbjogUHl0aG9uU2NyaXB0ZXJQbHVnaW4pIHtcclxuXHRcdHN1cGVyKGFwcCwgcGx1Z2luKTtcclxuXHRcdHRoaXMucGx1Z2luID0gcGx1Z2luO1xyXG5cdH1cclxuXHJcblx0ZGlzcGxheSgpOiB2b2lkIHtcclxuXHRcdGNvbnN0IHtjb250YWluZXJFbH0gPSB0aGlzO1xyXG5cclxuXHRcdGNvbnRhaW5lckVsLmVtcHR5KCk7XHJcblxyXG5cdFx0bmV3IFNldHRpbmcoY29udGFpbmVyRWwpXHJcblx0XHRcdC5zZXROYW1lKCdQeXRob24gU2NyaXB0IFBhdGgnKVxyXG5cdFx0XHQuc2V0RGVzYygnRGVmYXVsdHMgdG8gLm9ic2lkaWFuXFxcXHNjcmlwdHNcXFxccHl0aG9uJylcclxuXHRcdFx0LmFkZFRleHQodGV4dCA9PiB0ZXh0XHJcblx0XHRcdFx0LnNldFBsYWNlaG9sZGVyKCdFbnRlciBwYXRoJylcclxuXHRcdFx0XHQuc2V0VmFsdWUodGhpcy5wbHVnaW4uc2V0dGluZ3MucHl0aG9uUGF0aClcclxuXHRcdFx0XHQub25DaGFuZ2UoYXN5bmMgKHZhbHVlKSA9PiB7XHJcblx0XHRcdFx0XHR0aGlzLnBsdWdpbi5zZXR0aW5ncy5weXRob25QYXRoID0gdmFsdWU7XHJcblx0XHRcdFx0XHRhd2FpdCB0aGlzLnBsdWdpbi5zYXZlU2V0dGluZ3MoKTtcclxuXHRcdFx0XHR9KSk7XHJcblx0fVxyXG59XHJcbiJdLAogICJtYXBwaW5ncyI6ICI7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7QUFBQTtBQUFBO0FBQUE7QUFBQTtBQUFBO0FBQUEsc0JBQStHO0FBQy9HLFdBQXNCO0FBQ3RCLFNBQW9CO0FBQ3BCLDJCQUFxQjtBQU9yQixJQUFNLG1CQUEyQztBQUFBLEVBQ2hELFlBQVk7QUFDYjtBQUVBLElBQXFCLHVCQUFyQixjQUFrRCx1QkFBTztBQUFBLEVBS3hELGNBQXNCO0FBQ2YsUUFBSTtBQUVKLFFBQUksS0FBSyxJQUFJLE1BQU0sbUJBQW1CLG1DQUFtQjtBQUNyRCxpQkFBVyxLQUFLLElBQUksTUFBTSxRQUFRLFlBQVk7QUFBQSxJQUNsRCxPQUFPO0FBQ0gsWUFBTSxJQUFJLE1BQU0sNkJBQTZCO0FBQUEsSUFDakQ7QUFDQSxXQUFPLEdBQUc7QUFBQSxFQUNkO0FBQUEsRUFFSCxNQUFNLFNBQVM7QUFDZCxVQUFNLEtBQUssYUFBYTtBQUN4QixRQUFJLFdBQVcsS0FBSyxZQUFZO0FBQ2hDLFFBQUksc0JBQW1DLFVBQUssS0FBSyxLQUFLLElBQUksTUFBTSxXQUFXLFdBQVcsUUFBUTtBQUM5RixTQUFLLGtCQUF1QixVQUFLLFVBQVUsbUJBQW1CO0FBQzlELFNBQUssMEJBQTBCO0FBQy9CLFFBQUksS0FBSyxTQUFTLGNBQWMsSUFBSTtBQUNuQyxXQUFLLGtCQUF1QixVQUFLLFVBQVUsS0FBSyxTQUFTLFVBQVU7QUFDbkUsV0FBSywwQkFBMEIsS0FBSyxTQUFTO0FBQUEsSUFDOUMsT0FBTztBQUNOLFdBQUssa0JBQXVCLFVBQUssVUFBVSxtQkFBbUI7QUFDOUQsV0FBSywwQkFBMEI7QUFBQSxJQUNoQztBQUNBLFlBQVEsSUFBSSxLQUFLLHVCQUF1QjtBQUN4QyxRQUFJO0FBQ0gsWUFBTSxLQUFLLElBQUksTUFBTSxhQUFhLEtBQUssdUJBQXVCO0FBQUEsSUFFL0QsU0FBUyxPQUFQ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
